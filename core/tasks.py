from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    subject = "Welcome to Reminder App!"
    message = "Hi there! 🎉 Thanks for registering. We hope you enjoy using our service."
    from_email = "rishichilveri@gmail.com"
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    return f"Email sent to {email}"
    send_telegram_message(chat_id=1275635203, message=f"✅ New user registered with email: {email}")
