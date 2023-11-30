import os
from dotenv import load_dotenv

from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

load_dotenv()


# @shared_task
# def send_welcome_email(user_id):
#     try:
#         user = get_user_model().objects.get(pk=user_id)
#         subject = 'Welcome to Our Library!'
#         message = f'Hi {user.username}, thank you for registering in our library.'
#         from_email = os.getenv('EMAIL_HOST_USER')
#         to_email = [user.email]
#         send_mail(subject, message, from_email, to_email, fail_silently=False)
#         print(f"Sent welcome email to {user.username}")
#     except Exception as e:
#         print(f"Error sending welcome email: {e}")

@shared_task
def send_welcome_email():
    # from .models import CustomUser

    # user = CustomUser.objects.get(pk=user_id)
    return "Hello world"
