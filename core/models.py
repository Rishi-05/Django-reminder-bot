from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    telegram_id = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.username or f"User {self.telegram_id}"
