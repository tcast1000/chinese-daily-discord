"""
Tests for pronunciation.score — the pinyin-based scoring module.

Uses pypinyin ground truth, not hand-typed pinyin.
"""

import pytest
from pypinyin import Style, lazy_pinyin

from pronunciation.score import ScoreResult, SyllableScore, score_pronunciation


def _pinyin(hanzi: str) -> str:
    return " ".join(lazy_pinyin(hanzi, style=Style.TONE3, neutral_tone_with_five=True))


class TestPerfectMatch:
    def test_exact_same_text(self):
        result = score_pronunciation("你好", "你好")
        assert result.overall == 1.0
        assert all(s.score == 1.0 for s in result.per_syllable)

    def test_single_character(self):
        result = score_pronunciation("好", "好")
        assert result.overall == 1.0


class TestHomophone:
    def test_same_pinyin_different_characters(self):
        # 你好 and 拟好 have the same pinyin: ni3 hao3
        result = score_pronunciation("你好", "拟好")
        assert result.overall == 1.0


class TestWrongToneOnly:
    def test_third_vs_second_tone(self):
        # 你 (ni3) vs 尼 (ni2) — same initial/final, different tone
        # 好 stays the same
        result = score_pronunciation("你好", "尼好")
        # First syllable: initial=0.4 + final=0.4 + tone=0 = 0.8
        # Second syllable: perfect = 1.0
        # Mean = 0.9, length_penalty = 1.0, overall = 0.9
        assert 0.75 <= result.overall <= 0.95
        tone_misses = [s for s in result.per_syllable if not s.tone_match]
        assert len(tone_misses) >= 1

    def test_note_mentions_tones(self):
        result = score_pronunciation("你好", "尼好")
        assert "tone" in result.note.lower() or "Tone" in result.note


class TestWrongInitial:
    def test_different_initial_consonant(self):
        # 你 (ni3) vs 里 (li3) — different initial, same final+tone
        result = score_pronunciation("你好", "里好")
        # First syllable: initial=0 + final=0.4 + tone=0.2 = 0.6
        # Second syllable: perfect = 1.0
        # Mean = 0.8, length_penalty = 1.0
        assert 0.5 <= result.overall <= 0.85


class TestMissingSyllable:
    def test_heard_shorter_than_target(self):
        result = score_pronunciation("你好吗", "你好")
        assert result.overall < 1.0
        # Length penalty: 2/3 ≈ 0.67
        assert result.overall <= 0.7

    def test_length_penalty_present(self):
        full = score_pronunciation("你好", "你好")
        short = score_pronunciation("你好吗", "你好")
        assert short.overall < full.overall


class TestExtraSyllable:
    def test_heard_longer_than_target(self):
        result = score_pronunciation("你好", "你好吗")
        assert result.overall < 1.0

    def test_symmetry_with_missing(self):
        missing = score_pronunciation("你好吗", "你好")
        extra = score_pronunciation("你好", "你好吗")
        # Both should be penalized
        assert missing.overall < 1.0
        assert extra.overall < 1.0


class TestEmptyHeard:
    def test_empty_string(self):
        result = score_pronunciation("你好", "")
        assert result.overall == 0.0
        assert result.per_syllable == []

    def test_whitespace_only(self):
        result = score_pronunciation("你好", "   ")
        assert result.overall == 0.0


class TestNeutralTone:
    def test_mama(self):
        # 妈妈: ma1 ma5 (second is neutral when using neutral_tone_with_five)
        result = score_pronunciation("妈妈", "妈妈")
        assert result.overall == 1.0

    def test_mama_pinyin_format(self):
        result = score_pronunciation("妈妈", "妈妈")
        assert "ma1" in result.target_pinyin


class TestErhua:
    def test_naer_does_not_crash(self):
        # 哪儿 should not raise
        result = score_pronunciation("哪儿", "哪儿")
        assert result.overall == 1.0

    def test_nar_vs_na(self):
        # 哪儿 vs 哪 — slight mismatch but should not crash
        result = score_pronunciation("哪儿", "哪")
        assert isinstance(result.overall, float)
        assert result.overall < 1.0


class TestScoreResultStructure:
    def test_fields_present(self):
        result = score_pronunciation("你好", "你好")
        assert isinstance(result, ScoreResult)
        assert isinstance(result.overall, float)
        assert isinstance(result.per_syllable, list)
        assert isinstance(result.target_pinyin, str)
        assert isinstance(result.heard_pinyin, str)
        assert isinstance(result.note, str)

    def test_syllable_score_fields(self):
        result = score_pronunciation("你好", "你好")
        for s in result.per_syllable:
            assert isinstance(s, SyllableScore)
            assert isinstance(s.target, str)
            assert isinstance(s.initial_match, bool)
            assert isinstance(s.final_match, bool)
            assert isinstance(s.tone_match, bool)
            assert 0.0 <= s.score <= 1.0

    def test_overall_bounded(self):
        result = score_pronunciation("你好", "谢谢")
        assert 0.0 <= result.overall <= 1.0


class TestNoteHeuristics:
    def test_native_tier(self):
        result = score_pronunciation("你好", "你好")
        assert "native" in result.note.lower() or "excellent" in result.note.lower()

    def test_no_audio(self):
        result = score_pronunciation("你好", "")
        assert "no audio" in result.note.lower() or "mic" in result.note.lower()

    def test_note_always_present(self):
        result = score_pronunciation("你好吗", "谢谢你")
        assert len(result.note) > 0


class TestLongerPhrases:
    def test_full_sentence(self):
        result = score_pronunciation("我是学生", "我是学生")
        assert result.overall == 1.0
        assert len(result.per_syllable) == 4

    def test_partial_sentence(self):
        result = score_pronunciation("我是学生", "我是")
        assert result.overall < 1.0
        assert len(result.per_syllable) >= 2
