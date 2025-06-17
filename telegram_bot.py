import os
import django

# ✅ Set DJANGO_SETTINGS_MODULE and setup Django BEFORE importing any models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from core.models import TelegramUser
from django.db.utils import IntegrityError


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    username = user.username
    telegram_id = user.id

    if username:
        try:
            TelegramUser.objects.get_or_create(username=username, telegram_id=telegram_id)
        except IntegrityError:
            pass

    update.message.reply_text(
        f"Hello {user.first_name or 'there'}! I'm your Reminder Bot! Your Telegram ID is: {telegram_id}"
    )


def main():
    from django.conf import settings
    TELEGRAM_TOKEN = 'Replace with your bot token'  
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Ideally from .env
    if not TELEGRAM_TOKEN:
        # fallback for local testing
        TELEGRAM_TOKEN = "Replace with your bot token"  # 🛑 Don’t hardcode this in public repos

    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    print("🤖 Telegram bot is running...")
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
