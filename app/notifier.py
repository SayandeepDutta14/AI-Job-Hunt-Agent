
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID   = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    url  = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
       
    }
    try:
        response = requests.post(url, data=data, timeout=10)
        if response.status_code == 200:
            print("  Telegram: message sent ✅")
        else:
            print(f"  Telegram error: {response.text}")
    except Exception as e:
        print(f"  Telegram exception: {e}")
