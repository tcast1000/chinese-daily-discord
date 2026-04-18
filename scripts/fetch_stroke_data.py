"""
One-time downloader for stroke order JSON from hanzi-writer-data via jsDelivr.
Writes one file per character to stroke_data/<char>.json.

Run:  python scripts/fetch_stroke_data.py
"""

import json
import os
import sys
import time
import urllib.parse
import urllib.request

HERE   = os.path.dirname(os.path.abspath(__file__))
ROOT   = os.path.dirname(HERE)
OUTDIR = os.path.join(ROOT, "stroke_data")
CDN    = "https://cdn.jsdelivr.net/npm/hanzi-writer-data@2.0.1/{}.json"

sys.path.insert(0, ROOT)
from characters import CHARACTERS  # noqa: E402


def fetch_one(ch: str) -> bool:
    out = os.path.join(OUTDIR, f"{ch}.json")
    if os.path.exists(out):
        return True
    url = CDN.format(urllib.parse.quote(ch))
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = resp.read()
        json.loads(data)  # validate
        with open(out, "wb") as f:
            f.write(data)
        return True
    except Exception as e:
        print(f"  FAIL {ch}: {e}")
        return False


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    chars = sorted({c["char"] for c in CHARACTERS})
    print(f"Fetching {len(chars)} characters to {OUTDIR}")

    ok = fail = 0
    for i, ch in enumerate(chars, 1):
        if fetch_one(ch):
            ok += 1
        else:
            fail += 1
        if i % 50 == 0:
            print(f"  {i}/{len(chars)} done (ok={ok}, fail={fail})")
        time.sleep(0.02)

    print(f"Done. ok={ok}, fail={fail}")
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
