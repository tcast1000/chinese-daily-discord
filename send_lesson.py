"""
Chinese Daily Lesson Sender
Sends one Chinese character lesson per text, 3 times per day.

Schedule:
  Monday–Saturday: 3 new characters/day (slots 0, 1, 2)
  Sunday:          3 review characters (one per slot)
  Cycle:           600 characters covered in ~33 weeks, then repeats

Timezone handling:
  The GitHub Actions workflow fires at 6 UTC times (covering both PDT and PST)
  and passes the SLOT explicitly. The script checks whether the current Pacific
  UTC offset matches the cron trigger to avoid sending duplicates at DST boundaries.

Required environment variables:
  GMAIL_USER         - your Gmail address
  GMAIL_APP_PASSWORD - Gmail App Password (not your regular password)
  SMS_EMAIL          - carrier email-to-SMS address (e.g. 4087866039@vtext.com)
  SLOT               - 0, 1, or 2 (set by the workflow)
  EXPECT_PDT         - (optional) "1" for PDT cron, "0" for PST cron, for DST dedup
"""

import os
import sys
import smtplib
from email.mime.text import MIMEText
from datetime import date, datetime
from zoneinfo import ZoneInfo

from characters import CHARACTERS

# ── Configuration ─────────────────────────────────────────────────────────────

START_DATE = date(2026, 4, 10)   # First day of lessons
TIMEZONE   = "America/Los_Angeles"

CHARS_PER_DAY     = 3   # texts per day
NEW_DAYS_PER_WEEK = 6   # Monday–Saturday get new characters
# Sunday (day_of_week == 6) is always review

GMAIL_USER         = os.environ.get("GMAIL_USER", "").strip()
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "").strip()
SMS_EMAIL          = os.environ.get("SMS_EMAIL", "").strip()


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


# ── Message formatting ─────────────────────────────────────────────────────────

SLOT_LABEL = {0: "Morning", 1: "Afternoon", 2: "Evening"}
TONE_MARK  = {
    1: "— (flat)",
    2: "/ (rising)",
    3: "v (dip-rise)",
    4: "\\ (falling)",
    5: "(neutral)",
}

def format_message(char_data: dict, slot: int, is_review: bool = False) -> str:
    tone_desc  = TONE_MARK.get(char_data["tone"], "")
    time_label = SLOT_LABEL.get(slot, "")
    prefix     = "[REVIEW] " if is_review else ""
    week_label = f"Week {char_data['week']}: {char_data['group']}"

    lines = [
        f"{prefix}Chinese Daily — {time_label}",
        f"Char:    {char_data['char']}",
        f"Pinyin:  {char_data['pinyin']}  Tone {char_data['tone']} {tone_desc}",
        f"Meaning: {char_data['meaning']}",
        f"",
        f"Example:",
        f"  {char_data['example_cn']}",
        f"  {char_data['example_pinyin']}",
        f"  \"{char_data['example_en']}\"",
        f"",
        f"[{week_label}]",
    ]
    return "\n".join(lines)


# ── Sending ────────────────────────────────────────────────────────────────────

def send_sms(message: str):
    msg = MIMEText(message, "plain", "utf-8")
    msg["From"]    = GMAIL_USER
    msg["To"]      = SMS_EMAIL
    msg["Subject"] = ""

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            server.sendmail(GMAIL_USER, SMS_EMAIL, msg.as_string())
        print(f"Lesson sent to {SMS_EMAIL}")
    except smtplib.SMTPAuthenticationError:
        print("ERROR: Gmail authentication failed.")
        print("Make sure GMAIL_APP_PASSWORD is a Gmail App Password, not your regular password.")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR sending message: {e}")
        sys.exit(1)


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    # Validate credentials
    missing = [v for v in ["GMAIL_USER", "GMAIL_APP_PASSWORD", "SMS_EMAIL"]
               if not os.environ.get(v)]
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

    message = format_message(char_data, slot, is_review)

    # Print to console (safe for any terminal encoding)
    safe = lambda s: s.encode(sys.stdout.encoding or "utf-8", errors="replace") \
                      .decode(sys.stdout.encoding or "utf-8", errors="replace")
    print("=" * 42)
    print(safe(message))
    print("=" * 42)

    send_sms(message)


if __name__ == "__main__":
    main()
