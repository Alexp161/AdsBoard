from django.shortcuts import render
from .models import Ad
from django.core.mail import send_mail

def ad_list(request):
    ads = Ad.objects.all()
    return render(request, 'templates/ad_list.html', {'ads': ads})

send_mail(
    'Welcome to My Awesome App',
    'This is a welcome email. Thank you for signing up!',
    'alexeyp000@gmail.com',
    ['alexeyp000@gmail.com'],
    fail_silently=False,
)