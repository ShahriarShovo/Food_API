from django.urls import path
from authentication.views.user_register import register
from authentication.views.user_login import login

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]