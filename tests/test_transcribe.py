"""
Smoke tests for pronunciation.transcribe.

Tests that require audio fixtures skip gracefully when the fixture files
are missing. Drop recordings into tests/fixtures/audio/ to enable them.
"""

import importlib.util
from pathlib import Path

import pytest

FIXTURES_DIR = Path(__file__).parent / "fixtures" / "audio"

FIXTURE_FILES = {
    "nihao": FIXTURES_DIR / "nihao.m4a",
    "nihao_ma": FIXTURES_DIR / "nihao_ma.m4a",
    "xiexie": FIXTURES_DIR / "xiexie.m4a",
    "nihao_wrong_tones": FIXTURES_DIR / "nihao_wrong_tones.m4a",
}

_AUDIO_EXTENSIONS = [".wav", ".m4a", ".mp3", ".ogg", ".flac"]


def _find_fixture(path: Path) -> Path | None:
    for ext in _AUDIO_EXTENSIONS:
        candidate = path.with_suffix(ext)
        if candidate.exists():
            return candidate
    return None


def _resolve_fixture(name: str) -> Path:
    found = _find_fixture(FIXTURE_FILES[name])
    if found:
        return found
    pytest.skip(f"Fixture not found: {FIXTURE_FILES[name]} (any audio extension)")


skip_no_whisper = pytest.mark.skipif(
    importlib.util.find_spec("faster_whisper") is None,
    reason="faster-whisper not installed — run: pip install faster-whisper",
)


class TestTranscriptionResult:
    """Tests for the dataclass structure (no model needed)."""

    def test_dataclass_fields(self):
        from pronunciation.transcribe import TranscriptionResult

        result = TranscriptionResult(text="你好", segments=[], duration_s=1.5)
        assert result.text == "你好"
        assert result.segments == []
        assert result.duration_s == 1.5

    def test_defaults(self):
        from pronunciation.transcribe import TranscriptionResult

        result = TranscriptionResult(text="测试")
        assert result.segments == []
        assert result.duration_s == 0.0


@skip_no_whisper
class TestTranscribeWithFixtures:
    """Integration tests that run actual Whisper inference on fixture audio."""

    def test_nihao(self):
        path = _resolve_fixture("nihao")
        from pronunciation.transcribe import transcribe

        result = transcribe(path)
        assert len(result.text) > 0
        assert any(c >= "一" for c in result.text), \
            f"Expected Chinese characters, got: {result.text}"

    def test_nihao_ma(self):
        path = _resolve_fixture("nihao_ma")
        from pronunciation.transcribe import transcribe

        result = transcribe(path)
        assert len(result.text) > 0
        assert any(c >= "一" for c in result.text)

    def test_xiexie(self):
        path = _resolve_fixture("xiexie")
        from pronunciation.transcribe import transcribe

        result = transcribe(path)
        assert len(result.text) > 0
        assert any(c >= "一" for c in result.text)

    def test_wrong_tones_still_transcribes(self):
        path = _resolve_fixture("nihao_wrong_tones")
        from pronunciation.transcribe import transcribe

        result = transcribe(path)
        assert len(result.text) > 0

    def test_result_has_segments(self):
        path = _resolve_fixture("nihao")
        from pronunciation.transcribe import transcribe

        result = transcribe(path)
        assert isinstance(result.segments, list)
        assert result.duration_s >= 0

    def test_result_has_duration(self):
        path = _resolve_fixture("nihao_ma")
        from pronunciation.transcribe import transcribe

        result = transcribe(path)
        assert result.duration_s > 0
