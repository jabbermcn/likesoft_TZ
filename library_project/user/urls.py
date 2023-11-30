from django.urls import path
from .views import RegisterUserView

urlpatterns = [
    path('users/register/', RegisterUserView.as_view(), name='user-register'),
]
