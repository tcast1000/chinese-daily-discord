"""
Pinyin-based pronunciation scoring.

Pure functions — no Discord, no async, no I/O. Takes target hanzi + heard hanzi,
returns a structured score with per-syllable breakdown.
"""

from __future__ import annotations

from dataclasses import dataclass

from pypinyin import Style, lazy_pinyin
from pypinyin.style._tone_convert import to_finals, to_initials


@dataclass
class SyllableScore:
    target: str
    heard: str | None
    initial_match: bool
    final_match: bool
    tone_match: bool
    score: float


@dataclass
class ScoreResult:
    overall: float
    per_syllable: list[SyllableScore]
    target_pinyin: str
    heard_pinyin: str
    note: str


def _to_pinyin_list(hanzi: str) -> list[str]:
    return lazy_pinyin(hanzi, style=Style.TONE3, neutral_tone_with_five=True)


def _parse_syllable(syllable: str) -> tuple[str, str, int]:
    """Parse a TONE3 syllable into (initial, final, tone_number)."""
    if not syllable:
        return ("", "", 0)

    if syllable[-1].isdigit():
        tone = int(syllable[-1])
        base = syllable[:-1]
    else:
        tone = 5
        base = syllable

    if not base:
        return ("", "", tone)

    initial = to_initials(base, strict=True)
    final = to_finals(base, strict=True)

    # to_initials/to_finals can return empty for standalone vowels like "a", "e"
    # In that case the entire base is the final
    if not initial and not final:
        final = base

    return (initial, final, tone)


def _score_syllable(target: str, heard: str | None) -> SyllableScore:
    if heard is None:
        return SyllableScore(
            target=target, heard=None,
            initial_match=False, final_match=False, tone_match=False,
            score=0.0,
        )

    t_initial, t_final, t_tone = _parse_syllable(target)
    h_initial, h_final, h_tone = _parse_syllable(heard)

    initial_match = t_initial == h_initial
    final_match = t_final == h_final
    tone_match = t_tone == h_tone

    score = initial_match * 0.4 + final_match * 0.4 + tone_match * 0.2
    return SyllableScore(
        target=target, heard=heard,
        initial_match=initial_match, final_match=final_match, tone_match=tone_match,
        score=score,
    )


def _generate_note(per_syllable: list[SyllableScore], overall: float) -> str:
    if overall >= 0.95:
        return "Native-tier — excellent pronunciation!"

    if not per_syllable:
        return "No audio detected — try speaking closer to the mic."

    all_initials_match = all(s.initial_match for s in per_syllable if s.heard is not None)
    all_finals_match = all(s.final_match for s in per_syllable if s.heard is not None)
    any_tone_miss = any(not s.tone_match for s in per_syllable if s.heard is not None)
    finals_miss_count = sum(1 for s in per_syllable if s.heard is not None and not s.final_match)
    missing_count = sum(1 for s in per_syllable if s.heard is None)

    if missing_count > 0:
        return "Some syllables were missed — try speaking the full phrase clearly."

    if all_initials_match and all_finals_match and any_tone_miss:
        return "Tones need work — your consonants and vowels were right."

    if finals_miss_count >= len(per_syllable) / 2:
        return "Vowel sounds drifted — focus on mouth shape for each syllable."

    if overall >= 0.8:
        return "Close! A few small adjustments and you've got it."

    if overall >= 0.5:
        return "Good effort — keep practicing this phrase."

    return "This one's tricky — slow down and try one syllable at a time."


def score_pronunciation(target_hanzi: str, heard_hanzi: str) -> ScoreResult:
    """Score heard pronunciation against a target phrase."""
    if not heard_hanzi.strip():
        return ScoreResult(
            overall=0.0,
            per_syllable=[],
            target_pinyin=" ".join(_to_pinyin_list(target_hanzi)),
            heard_pinyin="",
            note="No audio detected — try speaking closer to the mic.",
        )

    target_py = _to_pinyin_list(target_hanzi)
    heard_py = _to_pinyin_list(heard_hanzi)

    max_len = max(len(target_py), len(heard_py))
    padded_target = target_py + [None] * (max_len - len(target_py))
    padded_heard = heard_py + [None] * (max_len - len(heard_py))

    per_syllable = [
        _score_syllable(t, h)
        for t, h in zip(padded_target, padded_heard)
        if t is not None
    ]

    # Also score extra heard syllables (not in target) as 0
    for h in padded_heard[len(target_py):]:
        if h is not None:
            per_syllable.append(SyllableScore(
                target="", heard=h,
                initial_match=False, final_match=False, tone_match=False,
                score=0.0,
            ))

    if not per_syllable:
        raw_mean = 0.0
    else:
        raw_mean = sum(s.score for s in per_syllable) / len(per_syllable)

    length_penalty = min(len(target_py), len(heard_py)) / max(len(target_py), len(heard_py))
    overall = raw_mean * length_penalty

    note = _generate_note(per_syllable, overall)

    return ScoreResult(
        overall=overall,
        per_syllable=per_syllable,
        target_pinyin=" ".join(target_py),
        heard_pinyin=" ".join(heard_py),
        note=note,
    )
