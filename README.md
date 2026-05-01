# Chinese Daily — Discord DM Lessons + AI Pronunciation Coach

A Discord bot that sends daily Mandarin character lessons and scores your pronunciation using Whisper speech recognition. Record yourself reading a phrase, and the bot transcribes your audio, compares it syllable-by-syllable against the target pinyin, and replies with detailed feedback — including tone accuracy, per-syllable scoring, and coaching notes.

**Daily lessons (via GitHub Actions — free):**
- 3 DMs per day (11 AM, 3 PM, 6 PM Pacific) with a new character, pinyin, tone, meaning, example sentence, stroke order diagram, and pronunciation audio
- 600 HSK 1-3 characters across ~33 themed weeks, then repeats
- Sunday = review day

**Pronunciation practice (persistent bot):**
- `/practice` — practice today's lesson phrase
- `/randompractice` — practice a random phrase from the 600-character bank
- `/practice phrase:你好吗` — practice any custom phrase
- `/stats` — view your scores, streaks, and progress over time
- Each phrase includes a sample pronunciation audio to listen to first

**How scoring works:**
- Whisper (faster-whisper, `small` model) transcribes your voice message into Chinese text
- pypinyin converts both target and heard text into pinyin syllables
- Each syllable is scored: initial consonant (40%), final vowel (40%), tone (20%)
- Length penalty applied if you say more or fewer syllables than the target
- Color-coded feedback per syllable + a one-line coaching note

---

## Setup

### Prerequisites

- Python 3.11+
- ffmpeg on PATH (`winget install ffmpeg` on Windows, `brew install ffmpeg` on macOS)
- A Discord bot token ([Developer Portal](https://discord.com/developers/applications))

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

The first time you run a practice command, faster-whisper downloads the `small` model (~460 MB) to `~/.cache/huggingface/`. Subsequent runs use the cached model.

### Step 2: Create a Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application**, name it (e.g. "Chinese Daily")
3. Go to the **Bot** tab → click **Reset Token** → copy the token
4. Under **Privileged Gateway Intents**, enable **Message Content Intent**
5. Go to **OAuth2 → URL Generator**:
   - Select scopes: **bot**, **applications.commands**
   - Select permissions: **Send Messages**, **Read Message History**, **Add Reactions**, **Attach Files**, **Use Slash Commands**
6. Open the generated URL to invite the bot to your server

### Step 3: Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and fill in:
```
DISCORD_TOKEN=your_bot_token
DISCORD_DM_USER_ID=your_discord_user_id
TEST_GUILD_ID=your_server_id
```

`TEST_GUILD_ID` is optional — it makes slash commands appear instantly in that server during development. Without it, global commands can take up to an hour to propagate.

### Step 4: Run the Bot

```bash
python bot.py
```

You should see:
```
Logged in as YourBot#1234 (ID: 123456789)
Synced 3 slash command(s) to guild ...
```

### Step 5: Daily Lessons (GitHub Actions)

For the automated daily DMs, push this repo to GitHub and add these secrets:

| Secret name          | Value                     |
|----------------------|---------------------------|
| `DISCORD_TOKEN`      | Bot token from Step 2     |
| `DISCORD_DM_USER_ID` | Your Discord user ID      |

The workflow in `.github/workflows/daily_chinese.yml` handles the schedule.

---

## Project Structure

```
bot.py                    — Persistent bot entry point (slash commands)
send_lesson.py            — Daily DM sender (GitHub Actions, stateless)
characters.py             — 600 HSK 1-3 characters with example sentences
cogs/practice.py          — /practice, /randompractice, /stats commands
pronunciation/
  transcribe.py           — Whisper transcription (singleton model, vad_filter)
  score.py                — Pinyin syllable-level scoring (pure functions)
  format.py               — Discord embed builder for score results
  db.py                   — SQLite score logging + streak tracking
tests/                    — pytest suite (run: python -m pytest tests/ -v)
scripts/
  fetch_stroke_data.py    — Downloads stroke order JSON from CDN
  generate_audio.py       — Generates pronunciation MP3s via edge-tts
```

## Running Tests

```bash
python -m pytest tests/ -v
```

Audio fixture tests require recordings in `tests/fixtures/audio/`. Without them, those tests skip gracefully.

## Adjusting the Schedule

Edit `.github/workflows/daily_chinese.yml` to change send times. The cron times are in UTC and fire at both PDT and PST offsets (the script auto-skips the wrong one).

## Keeping GitHub Actions Active

GitHub disables scheduled workflows after **60 days of repository inactivity**. The `keepalive.yml` workflow bumps a file monthly to prevent this.
