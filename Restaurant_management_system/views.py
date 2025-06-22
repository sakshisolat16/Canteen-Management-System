# I have created this file - Darshan
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html')



def send_test_email(request):
    send_mail(
        'Subject: Test Email',
        'This is a test email from Django.',
        'your_email@gmail.com',
        ['recipient@example.com'],
        fail_silently=False,
    )
    return HttpResponse("Test email sent successfully!")

