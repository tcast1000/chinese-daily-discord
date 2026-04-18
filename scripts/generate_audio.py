"""
One-time generator for character pronunciation MP3s via edge-tts.
Each MP3 contains: <character> <pause> <example sentence>
Writes audio/<char>.mp3 (skips existing files, so reruns are idempotent).

Run:  python scripts/generate_audio.py
"""

import asyncio
import os
import sys

import edge_tts

HERE   = os.path.dirname(os.path.abspath(__file__))
ROOT   = os.path.dirname(HERE)
OUTDIR = os.path.join(ROOT, "audio")
VOICE  = "zh-CN-XiaoxiaoNeural"
RATE   = "-15%"  # slow down slightly for learners

sys.path.insert(0, ROOT)
from characters import CHARACTERS  # noqa: E402


async def generate_one(char_data: dict) -> tuple[str, bool, str]:
    ch   = char_data["char"]
    path = os.path.join(OUTDIR, f"{ch}.mp3")
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return ch, True, "skip"

    # Full Chinese stop between the character and the example creates a natural pause.
    text = f"{ch}。{char_data['example_cn']}。"
    try:
        comm = edge_tts.Communicate(text, VOICE, rate=RATE)
        await comm.save(path)
        size = os.path.getsize(path)
        if size == 0:
            return ch, False, "empty output"
        return ch, True, f"{size}B"
    except Exception as e:
        if os.path.exists(path):
            os.remove(path)
        return ch, False, str(e)


async def main():
    os.makedirs(OUTDIR, exist_ok=True)
    total = len(CHARACTERS)
    print(f"Generating {total} audio files to {OUTDIR}")

    ok = fail = 0
    for i, cd in enumerate(CHARACTERS, 1):
        ch, success, msg = await generate_one(cd)
        if success:
            ok += 1
        else:
            fail += 1
            print(f"  FAIL {ch}: {msg}")
        if i % 25 == 0:
            print(f"  {i}/{total} (ok={ok}, fail={fail})")
        await asyncio.sleep(0.05)  # be polite to the endpoint

    print(f"Done. ok={ok}, fail={fail}")
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
