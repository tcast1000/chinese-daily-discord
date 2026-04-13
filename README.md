# Chinese Daily — Discord DM Lessons

Sends Chinese character lessons as Discord DMs 3 times a day — completely free via GitHub Actions.

**What you get each DM:**
- The character (汉字) displayed large
- Pinyin + tone description
- English meaning
- An example sentence (Chinese, pinyin, English)
- Theme label (grouped by topic across weeks)

**Schedule (Pacific Time):**
- 11 AM, 3 PM, 6 PM — one character per DM
- Monday–Saturday: 3 new characters per day
- Sunday: 3 review characters
- 600 characters across ~33 themed weeks, then the cycle repeats

---

## Setup (GitHub Actions)

### Step 1: Create a Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application**, name it (e.g. "Chinese Daily")
3. Go to the **Bot** tab → click **Reset Token** → copy the token
4. Under **Privileged Gateway Intents**, no special intents are needed
5. Go to **OAuth2 → URL Generator**:
   - Select scope: **bot**
   - Select permission: **Send Messages**
6. Open the generated URL to invite the bot to any server you're in

### Step 2: Get Your Discord User ID

1. Open Discord → **Settings → Advanced** → enable **Developer Mode**
2. Right-click your username anywhere → **Copy User ID**

### Step 3: Push This Folder to GitHub

1. Create a new **private** repository on GitHub
2. Push this folder to it

### Step 4: Add GitHub Secrets

In your GitHub repository, go to:
**Settings → Secrets and variables → Actions → New repository secret**

Add these two secrets:

| Secret name          | Value                              |
|----------------------|------------------------------------|
| `DISCORD_TOKEN`      | Bot token from Step 1              |
| `DISCORD_DM_USER_ID` | Your user ID from Step 2          |

### Step 5: Test It

Go to your GitHub repo → **Actions** tab → **Chinese Daily Lesson** → **Run workflow**

You should receive a Discord DM within a minute!

---

## Adjusting the Schedule

Edit `.github/workflows/daily_chinese.yml` to change send times. The cron times
are in UTC and fire at both PDT and PST offsets (the script auto-skips the wrong one).

## Customizing the Start Date

Edit `send_lesson.py` and change this line:
```python
START_DATE = date(2026, 4, 10)
```

## Keeping GitHub Actions Active

GitHub disables scheduled workflows after **60 days of repository inactivity**.
The `keepalive.yml` workflow bumps a file monthly to prevent this.
