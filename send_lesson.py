"""
Chinese Daily Lesson — Discord DM Bot
Sends one Chinese character lesson as a Discord DM, 3 times per day.

Schedule:
  Monday–Saturday: 3 new characters/day (slots 0, 1, 2)
  Sunday:          3 review characters (one per slot)
  Cycle:           600 characters covered in ~33 weeks, then repeats

Timezone handling:
  The GitHub Actions workflow fires at 6 UTC times (covering both PDT and PST)
  and passes the SLOT explicitly. The script checks whether the current Pacific
  UTC offset matches the cron trigger to avoid sending duplicates at DST boundaries.

Required environment variables:
  DISCORD_TOKEN      - your Discord bot token
  DISCORD_DM_USER_ID - Discord user ID to DM
  SLOT               - 0, 1, or 2 (set by the workflow)
  EXPECT_PDT         - (optional) "1" for PDT cron, "0" for PST cron, for DST dedup
"""

import asyncio
import io
import json
import os
import sys
from datetime import date, datetime
from zoneinfo import ZoneInfo

import discord

from characters import CHARACTERS

_HERE            = os.path.dirname(os.path.abspath(__file__))
STROKE_DATA_DIR  = os.path.join(_HERE, "stroke_data")
AUDIO_DIR        = os.path.join(_HERE, "audio")

# ── Configuration ─────────────────────────────────────────────────────────────

START_DATE = date(2026, 4, 10)   # First day of lessons
TIMEZONE   = "America/Los_Angeles"

CHARS_PER_DAY     = 3   # DMs per day
NEW_DAYS_PER_WEEK = 6   # Monday–Saturday get new characters
# Sunday (day_of_week == 6) is always review

DISCORD_TOKEN      = os.environ.get("DISCORD_TOKEN", "").strip()
DISCORD_DM_USER_ID = os.environ.get("DISCORD_DM_USER_ID", "").strip()


# ── DST dedup ────────────────────────────────────────────────────────────────

def is_correct_dst_trigger() -> bool:
    """
    Each slot fires twice per day (once at the PDT UTC offset, once at PST).
    The workflow passes EXPECT_PDT=1 for PDT crons, EXPECT_PDT=0 for PST crons.
    Compare against the current Pacific UTC offset to skip the wrong trigger.
    For workflow_dispatch (EXPECT_PDT is empty), always send.
    """
    expect_pdt = os.environ.get("EXPECT_PDT", "").strip()
    if not expect_pdt:
        return True  # manual trigger, always send

    now_pt = datetime.now(ZoneInfo(TIMEZONE))
    utc_offset_hours = now_pt.utcoffset().total_seconds() / 3600
    currently_pdt = (utc_offset_hours == -7)  # PDT = UTC-7, PST = UTC-8

    return currently_pdt == (expect_pdt == "1")


# ── Character selection ────────────────────────────────────────────────────────

def get_todays_character(slot: int):
    """
    Return (char_dict, is_review) for the given slot (0/1/2) based on today's date.
    """
    today    = date.today()
    day_num  = (today - START_DATE).days

    if day_num < 0:
        print(f"Lessons start on {START_DATE}. Nothing to send today.")
        return None, False

    total        = len(CHARACTERS)
    week_num     = day_num // 7
    day_of_week  = day_num % 7              # 0–5 = new, 6 = review

    chars_per_week = NEW_DAYS_PER_WEEK * CHARS_PER_DAY  # 18

    if day_of_week == 6:
        # ── Review day ────────────────────────────────────────────────────────
        covered = week_num * chars_per_week
        if covered == 0:
            char_idx = slot % total
        else:
            review_pool = max(CHARS_PER_DAY, covered - chars_per_week)
            char_idx = (week_num * 11 + slot * 17) % review_pool
        return CHARACTERS[char_idx % total], True
    else:
        # ── New character ─────────────────────────────────────────────────────
        char_idx = (week_num * chars_per_week + day_of_week * CHARS_PER_DAY + slot) % total
        return CHARACTERS[char_idx], False


# ── Stroke order rendering ────────────────────────────────────────────────────

# hanzi-writer-data uses a 1024x1024 Cartesian (Y-up) coordinate space.
# Standard SVG render transform flips Y and offsets to the 0-900 character band.
_HANZI_INNER_TRANSFORM = "translate(0, 900) scale(1, -1)"
_PANEL_PX     = 160
_MAX_PER_ROW  = 10
_PNG_SCALE    = 2   # 2x for retina crispness


def render_stroke_order_png(char: str) -> bytes | None:
    """Render a progressive stroke-order diagram (1 panel per stroke) as PNG bytes.
    Returns None if the character has no stroke data file."""
    path = os.path.join(STROKE_DATA_DIR, f"{char}.json")
    if not os.path.exists(path):
        return None

    try:
        import resvg_py
    except ImportError:
        print("WARN: resvg_py not installed; skipping stroke order image.")
        return None

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    strokes = data.get("strokes") or []
    n = len(strokes)
    if n == 0:
        return None

    cols = min(n, _MAX_PER_ROW)
    rows = (n + _MAX_PER_ROW - 1) // _MAX_PER_ROW
    w = cols * _PANEL_PX
    h = rows * _PANEL_PX
    inner_scale = _PANEL_PX / 1024.0

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w}" height="{h}">',
        f'<rect width="{w}" height="{h}" fill="white"/>',
    ]
    for i in range(n):
        row = i // _MAX_PER_ROW
        col = i % _MAX_PER_ROW
        x0  = col * _PANEL_PX
        y0  = row * _PANEL_PX
        parts.append(
            f'<rect x="{x0 + 0.5}" y="{y0 + 0.5}" '
            f'width="{_PANEL_PX - 1}" height="{_PANEL_PX - 1}" '
            f'fill="none" stroke="#e5e5e5"/>'
        )
        parts.append(
            f'<g transform="translate({x0},{y0}) scale({inner_scale}) '
            f'{_HANZI_INNER_TRANSFORM}">'
        )
        for j in range(i + 1):
            color = "#d32f2f" if j == i else "#c8c8c8"
            parts.append(f'<path d="{strokes[j]}" fill="{color}"/>')
        parts.append('</g>')
        parts.append(
            f'<text x="{x0 + 6}" y="{y0 + 16}" font-family="Helvetica" '
            f'font-size="12" fill="#888">{i + 1}</text>'
        )
    parts.append('</svg>')
    svg = "".join(parts)

    png = resvg_py.svg_to_bytes(
        svg_string=svg,
        width=w * _PNG_SCALE,
        height=h * _PNG_SCALE,
    )
    return bytes(png) if png else None


def load_pronunciation_mp3(char: str) -> bytes | None:
    """Return pre-generated MP3 bytes for the character, or None if missing."""
    path = os.path.join(AUDIO_DIR, f"{char}.mp3")
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return None
    with open(path, "rb") as f:
        return f.read()


# ── Embed formatting ─────────────────────────────────────────────────────────

SLOT_LABEL = {0: "Morning", 1: "Afternoon", 2: "Evening"}
TONE_MARK  = {
    1: "— (flat)",
    2: "/ (rising)",
    3: "v (dip-rise)",
    4: "\\ (falling)",
    5: "(neutral)",
}

# Colors per slot for visual distinction
SLOT_COLOR = {0: 0xE74C3C, 1: 0xF39C12, 2: 0x3498DB}  # red, orange, blue


STROKE_ATTACHMENT_NAME = "stroke_order.png"
AUDIO_ATTACHMENT_NAME  = "pronunciation.mp3"


def build_embed(char_data: dict, slot: int, is_review: bool = False,
                has_stroke_image: bool = False) -> discord.Embed:
    tone_desc  = TONE_MARK.get(char_data["tone"], "")
    time_label = SLOT_LABEL.get(slot, "")
    prefix     = "\U0001f504 REVIEW — " if is_review else ""
    week_label = f"Week {char_data['week']}: {char_data['group']}"

    embed = discord.Embed(
        title=f"{prefix}Chinese Daily — {time_label}",
        color=SLOT_COLOR.get(slot, 0x5865F2),
    )

    embed.add_field(
        name="Character",
        value=f"# {char_data['char']}",
        inline=False,
    )
    embed.add_field(name="Pinyin", value=char_data["pinyin"], inline=True)
    embed.add_field(
        name="Tone",
        value=f"{char_data['tone']} {tone_desc}",
        inline=True,
    )
    embed.add_field(name="Meaning", value=char_data["meaning"], inline=False)

    example = (
        f"**{char_data['example_cn']}**\n"
        f"{char_data['example_pinyin']}\n"
        f"*\"{char_data['example_en']}\"*"
    )
    embed.add_field(name="Example", value=example, inline=False)

    if has_stroke_image:
        embed.set_image(url=f"attachment://{STROKE_ATTACHMENT_NAME}")

    embed.set_footer(text=week_label)

    return embed


# ── Sending ────────────────────────────────────────────────────────────────────

async def send_discord_dm(embed: discord.Embed,
                          stroke_png: bytes | None = None,
                          audio_mp3: bytes | None = None):
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        try:
            user = await client.fetch_user(int(DISCORD_DM_USER_ID))
            files = []
            if stroke_png:
                files.append(discord.File(
                    io.BytesIO(stroke_png),
                    filename=STROKE_ATTACHMENT_NAME,
                ))
            if audio_mp3:
                files.append(discord.File(
                    io.BytesIO(audio_mp3),
                    filename=AUDIO_ATTACHMENT_NAME,
                ))
            await user.send(embed=embed, files=files) if files else await user.send(embed=embed)
            print(f"DM sent to user {DISCORD_DM_USER_ID}")
        except discord.Forbidden:
            print("ERROR: Bot cannot DM this user. Make sure DMs are enabled.")
            await client.close()
            sys.exit(1)
        except Exception as e:
            print(f"ERROR sending DM: {e}")
            await client.close()
            sys.exit(1)
        await client.close()

    await client.start(DISCORD_TOKEN)


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    # Validate credentials
    missing = [v for v in ["DISCORD_TOKEN", "DISCORD_DM_USER_ID"]
               if not os.environ.get(v, "").strip()]
    if missing:
        print(f"ERROR: Missing environment variables: {', '.join(missing)}")
        sys.exit(1)

    # Determine slot
    slot_env = os.environ.get("SLOT", "").strip()
    if not slot_env:
        print("ERROR: SLOT environment variable is required (0, 1, or 2)")
        sys.exit(1)
    slot = int(slot_env)

    # DST dedup: both PDT and PST crons fire; skip the wrong one
    if not is_correct_dst_trigger():
        now_pt = datetime.now(ZoneInfo(TIMEZONE))
        print(f"DST dedup: wrong offset trigger. Current: {now_pt.strftime('%Z')}. Skipping.")
        sys.exit(0)

    if slot not in (0, 1, 2):
        print("ERROR: SLOT must be 0, 1, or 2")
        sys.exit(1)

    char_data, is_review = get_todays_character(slot)
    if char_data is None:
        return

    override = os.environ.get("CHAR_OVERRIDE", "").strip()
    if override:
        match = next((c for c in CHARACTERS if c["char"] == override), None)
        if match is None:
            print(f"ERROR: CHAR_OVERRIDE {override!r} not in CHARACTERS")
            sys.exit(1)
        char_data, is_review = match, False
        print(f"CHAR_OVERRIDE active: sending {override}")

    stroke_png = render_stroke_order_png(char_data["char"])
    audio_mp3  = load_pronunciation_mp3(char_data["char"])
    embed = build_embed(char_data, slot, is_review,
                        has_stroke_image=stroke_png is not None)

    # Print summary to console
    safe = lambda s: s.encode(sys.stdout.encoding or "utf-8", errors="replace") \
                      .decode(sys.stdout.encoding or "utf-8", errors="replace")
    print("=" * 42)
    print(safe(f"{char_data['char']} — {char_data['pinyin']} — {char_data['meaning']}"))
    print(f"stroke image: {'yes (' + str(len(stroke_png)) + ' bytes)' if stroke_png else 'no'}")
    print(f"audio:        {'yes (' + str(len(audio_mp3)) + ' bytes)' if audio_mp3 else 'no'}")
    print("=" * 42)

    asyncio.run(send_discord_dm(embed, stroke_png, audio_mp3))


if __name__ == "__main__":
    main()
