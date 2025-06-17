import os
import requests
from decouple import config

TELEGRAM_BOT_TOKEN = config("TELEGRAM_BOT_TOKEN")  # store in .env
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

def send_telegram_message(chat_id, message):
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(BASE_URL, data=payload)
    return response.json()
