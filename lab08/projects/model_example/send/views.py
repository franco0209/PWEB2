from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    send_mail("Hello Django!!", "Hello there",
               "facs02222@gmail.com",
               ["fcahua@unsa.edu.pe"],
               fail_silently=False)

    return render(request, "send/index.html")