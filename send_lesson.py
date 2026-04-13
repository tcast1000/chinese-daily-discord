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
import os
import sys
from datetime import date, datetime
from zoneinfo import ZoneInfo

import discord

from characters import CHARACTERS

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


def build_embed(char_data: dict, slot: int, is_review: bool = False) -> discord.Embed:
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

    embed.set_footer(text=week_label)

    return embed


# ── Sending ────────────────────────────────────────────────────────────────────

async def send_discord_dm(embed: discord.Embed):
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        try:
            user = await client.fetch_user(int(DISCORD_DM_USER_ID))
            await user.send(embed=embed)
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

    embed = build_embed(char_data, slot, is_review)

    # Print summary to console
    safe = lambda s: s.encode(sys.stdout.encoding or "utf-8", errors="replace") \
                      .decode(sys.stdout.encoding or "utf-8", errors="replace")
    print("=" * 42)
    print(safe(f"{char_data['char']} — {char_data['pinyin']} — {char_data['meaning']}"))
    print("=" * 42)

    asyncio.run(send_discord_dm(embed))


if __name__ == "__main__":
    main()
