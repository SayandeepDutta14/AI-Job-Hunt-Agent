# 🚀 AI Job Hunt Agent

A smart AI agent that automatically finds backend developer remote jobs every 3 hours and sends them directly to your Telegram.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)
![Gemini](https://img.shields.io/badge/Gemini-AI-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

- 🔍 Scrapes remote backend jobs from Jobicy API every 3 hours
- 🤖 Gemini AI-powered filtering — intelligently detects relevant backend jobs
- 📬 Instant Telegram notifications with job title, description and link
- 🚫 Duplicate detection — never sends the same job twice
- ⚡ Built with FastAPI — lightweight and fast
- 💸 100% free — no paid API needed

---

## 📸 How It Works

```text
Every 3 hours
      ↓
Fetch jobs from Jobicy API
(python, backend, fastapi, django, nodejs, api, springboot)
      ↓
Gemini AI filtering
(removes unrelated jobs intelligently)
      ↓
Send new jobs to Telegram
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core language |
| FastAPI | Web framework |
| APScheduler | Job scheduling every 3 hours |
| Jobicy API | Free remote job listings |
| Gemini API | AI-based job filtering |
| Telegram Bot API | Notifications |
| python-dotenv | Environment variables |

---

## 📁 Project Structure

```text
upwork-ai-agent/
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI app entry point
│   ├── scraper.py      # Fetches jobs from Jobicy API
│   ├── ai_filter.py    # Gemini AI-based job filtering
│   ├── notifier.py     # Sends Telegram messages
│   └── scheduler.py    # Runs agent every 3 hours
├── .env.example        # Environment variable template
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/upwork-ai-agent.git
cd upwork-ai-agent
```

### 2. Create virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create your Telegram Bot

1. Open Telegram and search `@BotFather`
2. Send `/newbot` and follow the steps
3. Copy your **BOT TOKEN**
4. Send a message to your bot
5. Open this URL in browser:

```text
https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
```

6. Copy your **chat id** from the response

---

### 5. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env`:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here
GEMINI_API_KEY=your_gemini_api_key_here
```

---

### 5.1 Add Gemini API Key

Get your free Gemini API key from Google AI Studio:

https://aistudio.google.com/app/apikey

Add this to your `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

### 6. Run the agent

```bash
uvicorn app.main:app --reload
```

The agent will:

- Start immediately and check for jobs
- Run automatically every 3 hours
- Send new backend jobs to your Telegram

---

## 🌐 Deploy on Railway (Free, 24/7)

1. Push your code to GitHub
2. Go to https://railway.app and sign in with GitHub
3. Click **New Project → Deploy from GitHub repo**
4. Select your repository
5. Go to **Variables** tab and add:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
   - `GEMINI_API_KEY`
6. Railway will auto-deploy and run 24/7

---

## 🔧 Customization

### Add more job keywords

Edit `app/scraper.py`:

```python
SEARCH_TAGS = [
    "python",
    "backend",
    "fastapi",
    "django",
    "nodejs",
    "your-tag-here"
]
```

---

### Change Gemini filtering prompt

Edit `app/ai_filter.py` to customize how Gemini evaluates jobs.

---

### Change check interval

Edit `app/scheduler.py`:

```python
scheduler.add_job(run_agent, "interval", hours=3)
```

---

## 📬 Example Telegram Notification

```text
🚀 Backend Gig Found!

📝 Senior Backend Engineer @ GitLab

📄 We are looking for a Senior Backend Engineer
to join our team. You will work on Python-based
microservices and REST APIs...

🔗 https://jobicy.com/jobs/12345
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

1. Fork the repo
2. Create your branch:

```bash
git checkout -b feature/amazing-feature
```

3. Commit your changes:

```bash
git commit -m "Add amazing feature"
```

4. Push to the branch:

```bash
git push origin feature/amazing-feature
```

5. Open a Pull Request

---

## 📄 License

MIT License — free to use, modify and distribute.

---

## 👨‍💻 Author

Built by [Sayandeep Dutta](https://github.com/sayandeepdutta14)

---

## ⭐ If this helped you, give it a star!
