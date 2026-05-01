# CLAUDE.md

## Project
Discord bot that posts a daily Mandarin phrase and scores user pronunciation.

## Stack
- discord.py 2.x
- faster-whisper (model: small, lang: zh)
- pypinyin
- pytest

## Hard rules
- CPU-bound work (Whisper, scoring) MUST run in `asyncio.to_thread`. Never block the event loop.
- The Whisper model is loaded once as a module-level singleton. Do not re-instantiate per call.
- All scoring logic lives in `pronunciation/score.py` as pure functions. No Discord types in there.
- `vad_filter=True` on every transcribe call — Whisper hallucinates on silence otherwise.
- Don't refactor existing daily-post logic without asking.
- Before declaring a phase done: run `pytest` AND manually invoke the relevant CLI/command.

## Conventions
- Type hints everywhere.
- Dataclasses for structured returns, not dicts.
- f-strings, no `.format()`.
- Tempfiles via `tempfile.TemporaryDirectory`, never leave audio on disk.

## Testing
- Audio fixtures live in `tests/fixtures/audio/`.
- Use `pypinyin` ground truth in scoring tests, not hand-typed pinyin.
- DB tests use a temp database via pytest fixture — never touch production db.

## Architecture
- `send_lesson.py` runs on GitHub Actions (stateless, 3x/day). Do not add Discord listeners here.
- `bot.py` is the persistent bot entry point. All interactive features go through cogs.
- `pronunciation/` contains pure logic modules (transcribe, score, format, db). No Discord imports except in format.py.
