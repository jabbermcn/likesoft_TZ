from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_welcome_email


class CustomUser(AbstractUser):
    """Модель кастомного пользователя."""

    email = models.EmailField(unique=True)
    registration_date = models.DateTimeField(default=timezone.now)

    def str(self):
        return self.username


# @receiver(post_save, sender=CustomUser)
# def send_welcome_email_to_new_user(sender, instance, created, **kwargs):
#     if created:
#         send_welcome_email.delay(instance.id)
