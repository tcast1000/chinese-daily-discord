"""
Whisper-based transcription for Chinese audio.

Uses faster-whisper (CTranslate2 backend) with the "small" model.
The model is loaded once as a module-level singleton to avoid
re-initialization on every call.

CLI usage:
    python -m pronunciation.transcribe <audio_path>
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from pathlib import Path

from faster_whisper import WhisperModel

_model: WhisperModel | None = None


def _get_model() -> WhisperModel:
    global _model
    if _model is None:
        _model = WhisperModel("small", device="cpu", compute_type="int8")
    return _model


@dataclass
class TranscriptionResult:
    text: str
    segments: list[dict] = field(default_factory=list)
    duration_s: float = 0.0


def transcribe(audio_path: Path) -> TranscriptionResult:
    """Transcribe a Chinese audio file and return structured results."""
    model = _get_model()
    segments_iter, info = model.transcribe(
        str(audio_path),
        language="zh",
        vad_filter=True,
    )

    segments = []
    full_text_parts = []
    for seg in segments_iter:
        segments.append({
            "start": seg.start,
            "end": seg.end,
            "text": seg.text.strip(),
        })
        full_text_parts.append(seg.text.strip())

    return TranscriptionResult(
        text="".join(full_text_parts),
        segments=segments,
        duration_s=info.duration,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Transcribe Chinese audio with Whisper")
    parser.add_argument("audio_path", type=Path, help="Path to an audio file")
    args = parser.parse_args()

    if not args.audio_path.exists():
        print(f"File not found: {args.audio_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Loading model (first run downloads ~460 MB)...")
    result = transcribe(args.audio_path)
    print(f"Text: {result.text}")
    print(f"Duration: {result.duration_s:.1f}s")
    print(f"Segments: {len(result.segments)}")
    for seg in result.segments:
        print(f"  [{seg['start']:.1f}s - {seg['end']:.1f}s] {seg['text']}")


if __name__ == "__main__":
    main()
