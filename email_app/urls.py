from django.urls import path
from email_app.views import send_email

urlpatterns = [
    path('', send_email, name='send_email')
]