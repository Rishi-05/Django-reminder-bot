import os
import django
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import CallbackContext
from core.models import TelegramUser
from django.db.utils import IntegrityError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # adjust if your settings module is different
django.setup()

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    username = user.username
    telegram_id = user.id

    # Save to DB if not exists
    if username:
        try:
            TelegramUser.objects.get_or_create(username=username, telegram_id=telegram_id)
        except IntegrityError:
            pass  # Prevent crashing if DB constraints cause issues

    update.message.reply_text(
        f"Hello {user.first_name or 'there'}! I'm your Reminder Bot! Your Telegram ID is: {telegram_id}"
    )

def main():
    from django.conf import settings
    TELEGRAM_TOKEN = 'Replace with your bot token'  
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    print("🤖 Telegram bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
