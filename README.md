# Chinese Daily — Free SMS Chinese Lessons

Sends one Chinese character lesson per day to your phone via text message — completely free.

**What you get each day:**
- The character (汉字)
- Pinyin + tone description
- English meaning
- An example sentence (Chinese, pinyin, English)
- Theme label (grouped by topic across weeks)

**Schedule:**
- Monday–Saturday: 1 new character per day
- Sunday: review of an earlier character
- 200 characters across 33 themed weeks, then the cycle repeats

---

## Setup (GitHub Actions — Runs in the Cloud, No Computer Needed)

### Step 1: Create a Gmail App Password

1. Enable 2-Factor Authentication on your Google account:
   https://myaccount.google.com/security

2. Generate an App Password:
   https://myaccount.google.com/apppasswords
   - Choose any name (e.g. "Chinese Daily")
   - Copy the 16-character code it gives you

### Step 2: Find Your Carrier's SMS Email Gateway

Replace `10digitnumber` with your actual phone number (no dashes):

| Carrier     | Email address                            |
|-------------|------------------------------------------|
| AT&T        | 10digitnumber@txt.att.net                |
| T-Mobile    | 10digitnumber@tmomail.net                |
| Verizon     | 10digitnumber@vtext.com                  |
| Sprint      | 10digitnumber@messaging.sprintpcs.com    |
| Cricket     | 10digitnumber@mms.cricketwireless.net    |
| Boost       | 10digitnumber@sms.myboostmobile.com      |
| Metro PCS   | 10digitnumber@mymetropcs.com             |
| US Cellular | 10digitnumber@email.uscc.net             |

### Step 3: Push This Folder to GitHub

1. Create a new **private** repository on GitHub (github.com → New repository)
2. Push this `chinese_daily` folder (or the whole `Automation` folder) to it

### Step 4: Add GitHub Secrets

In your GitHub repository, go to:
**Settings → Secrets and variables → Actions → New repository secret**

Add these three secrets:

| Secret name        | Value                                     |
|--------------------|-------------------------------------------|
| `GMAIL_USER`       | your Gmail address (e.g. you@gmail.com)   |
| `GMAIL_APP_PASSWORD` | the 16-char App Password from Step 1   |
| `SMS_EMAIL`        | your carrier SMS email from Step 2        |

### Step 5: Adjust the Send Time (Optional)

Edit `.github/workflows/daily_chinese.yml` and change the cron line:

```yaml
- cron: '0 14 * * *'   # 14:00 UTC = 9 AM Eastern
```

Common conversions (for 9 AM your time):
- 9 AM Eastern:  `0 14 * * *`
- 9 AM Central:  `0 15 * * *`
- 9 AM Mountain: `0 16 * * *`
- 9 AM Pacific:  `0 17 * * *`

### Step 6: Test It

Go to your GitHub repo → **Actions** tab → **Daily Chinese Lesson** → **Run workflow**

You should receive a text message within a minute!

---

## Alternative: Run Locally with Windows Task Scheduler

If you prefer to run it on your own computer instead of GitHub:

### 1. Set up environment variables (one-time)

Open PowerShell as Administrator and run:
```powershell
[Environment]::SetEnvironmentVariable("GMAIL_USER", "you@gmail.com", "User")
[Environment]::SetEnvironmentVariable("GMAIL_APP_PASSWORD", "your16charpassword", "User")
[Environment]::SetEnvironmentVariable("SMS_EMAIL", "5551234567@tmomail.net", "User")
```

### 2. Create the scheduled task

Open PowerShell and run (adjust paths as needed):
```powershell
$action = New-ScheduledTaskAction -Execute "python" `
  -Argument "C:\Users\tcast\OneDrive\Desktop\Vibe Coding\Automation\chinese_daily\send_lesson.py" `
  -WorkingDirectory "C:\Users\tcast\OneDrive\Desktop\Vibe Coding\Automation\chinese_daily"

$trigger = New-ScheduledTaskTrigger -Daily -At "9:00AM"

Register-ScheduledTask -TaskName "Chinese Daily Lesson" `
  -Action $action -Trigger $trigger -RunLevel Highest
```

> Note: Your computer must be on and connected at 9 AM for this to run.

---

## Keeping GitHub Actions Active

GitHub disables scheduled workflows after **60 days of repository inactivity**.
To prevent this, either:
- Make a small commit every couple of months, OR
- Go to the Actions tab and manually click "Run workflow" occasionally

---

## Customizing the Start Date

Edit `send_lesson.py` and change this line to your preferred start date:
```python
START_DATE = date(2026, 4, 11)
```

The system automatically figures out which character to send based on
how many days have passed since the start date — no database needed.
