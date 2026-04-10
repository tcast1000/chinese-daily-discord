"""
Chinese Daily Lesson Sender
Sends one Chinese character lesson per text, 3 times per day.

Schedule:
  Monday–Saturday: 3 new characters/day (slots 0, 1, 2)
  Sunday:          3 review characters (one per slot)
  Cycle:           200 characters covered in ~11 weeks, then repeats

Required environment variables:
  GMAIL_USER         - your Gmail address
  GMAIL_APP_PASSWORD - Gmail App Password (not your regular password)
  SMS_EMAIL          - carrier email-to-SMS address (e.g. 4087866039@vtext.com)
  SLOT               - which message of the day: 0 (11 AM), 1 (3 PM), 2 (6 PM)
"""

import os
import sys
import smtplib
from email.mime.text import MIMEText
from datetime import date

from characters import CHARACTERS

# ── Configuration ─────────────────────────────────────────────────────────────

START_DATE = date(2026, 4, 10)   # First day of lessons

CHARS_PER_DAY  = 3   # texts per day
NEW_DAYS_PER_WEEK = 6  # Monday–Saturday get new characters
# Sunday (day_of_week == 6) is always review

GMAIL_USER         = os.environ.get("GMAIL_USER", "").strip()
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "").strip()
SMS_EMAIL          = os.environ.get("SMS_EMAIL", "").strip()


# ── Character selection ────────────────────────────────────────────────────────

def get_todays_character(slot: int):
    """
    Return (char_dict, is_review) for the given slot (0/1/2) based on today's date.

    New-character days (Mon–Sat):
      char index = week_num * 18 + day_of_week * 3 + slot

    Review day (Sun):
      picks a deterministic character from an earlier week
    """
    today    = date.today()
    day_num  = (today - START_DATE).days

    if day_num < 0:
        print(f"Lessons start on {START_DATE}. Nothing to send today.")
        return None, False

    total        = len(CHARACTERS)          # 200
    week_num     = day_num // 7
    day_of_week  = day_num % 7              # 0–5 = new, 6 = review

    chars_per_week = NEW_DAYS_PER_WEEK * CHARS_PER_DAY  # 18

    if day_of_week == 6:
        # ── Review day ────────────────────────────────────────────────────────
        covered = week_num * chars_per_week
        if covered == 0:
            char_idx = slot % total
        else:
            # Skip the most recent week; pick deterministically from earlier
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
    # Validate config
    missing = [v for v in ["GMAIL_USER", "GMAIL_APP_PASSWORD", "SMS_EMAIL", "SLOT"]
               if not os.environ.get(v)]
    if missing:
        print(f"ERROR: Missing environment variables: {', '.join(missing)}")
        sys.exit(1)

    slot = int(os.environ["SLOT"])
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
