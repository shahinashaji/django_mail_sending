from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail


def send_email(request):
    if request.method == 'POST':
        recipient = request.POST.get('receiver_mail')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email_from = settings.EMAIL_HOST_USER
        mail_status = send_mail(subject, message, email_from, [recipient], fail_silently=False)
        return render(request, 'index.html', {'status': mail_status})
    else:
        return render(request, 'index.html', {})
