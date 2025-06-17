# Django Reminder Bot 🧠📲

A backend project built with Django, DRF, Celery, and Telegram Bot API. It allows users to register, manage tasks, receive reminder notifications via Telegram, and background email sending.

---

## 📦 Features

- JWT Authentication
- REST API (public and protected endpoints)
- Celery with RabbitMQ
- Sends welcome email on registration
- Telegram bot integration

---

## 🛠️ Tech Stack

- Django & Django REST Framework
- SimpleJWT for authentication
- Celery + RabbitMQ
- PostgreSQL
- Telegram Bot API
- Email (SMTP)

---


## 🔧 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/django-reminder-bot.git
cd django-reminder-bot 
```

### 2. Create and activate a virtual environment
```
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate #mac or linux
```

### 3. Message Broker Setup (RabbitMQ + Erlang)
This project uses Celery with RabbitMQ as the message broker to handle background tasks like sending welcome emails.
```
1. Install Erlang
Go to the official Erlang site: https://www.erlang.org/downloads

2. Install RabbitMQ
Go to: https://www.rabbitmq.com/download.html

3. Enable RabbitMQ Management Plugin (Optional but recommended)
This gives you a web UI at http://localhost:15672/

rabbitmq-server.bat
rabbitmq-plugins enable rabbitmq_management
Username: guest
Password: guest
```
### 4. Install dependencies
```
pip install -r requirements.txt
```
### 5.  Add .env file
```
SECRET_KEY=your-django-secret-key
DEBUG=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password-or-app-password
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
```

### 6. Migrate Database
```
python manage.py migrate
```

### 7. Start RabbitMQ Server
```
Run rabbitmq-server.bat or ensure RabbitMQ is running.
1. http://localhost:15672/
```

### 8. Start Celery Worker
```
celery -A config worker --loglevel=info --pool=solo
```

### 9. Run the Server
```
python manage.py runserver
1. Visit: http://127.0.0.1:8000/
2. http://127.0.0.1:8000/api/accounts/register/
3. http://127.0.0.1:8000/api/accounts/login/
4. http://127.0.0.1:8000/api/token/ (registered credentials)
```
### 10. Run Telegram Bot
```
python telegram_bot.py
```

### 11. API Endpoints
```
Method	     Endpoint	                 Description
POST	/api/accounts/register/	    Register a new user
POST	/api/accounts/login/	    Obtain JWT token
GET	/api/core/secret/	    Protected view (requires token)
POST	/api/token/refresh/	    Refresh JWT token
```

### 12. Environment Variables

Rename `.env.example` to `.env` and fill in your actual credentials:

```bash
cp .env.example .env
```
