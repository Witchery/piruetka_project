from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
def index(request):
    return HttpResponse("Hello, world. You're at the webapp index")
"""
"""
def home(request):
    return render(request, 'Web_App/home.html')
"""

# Create views here:
def index(request):
    context = {"home_page": "active"}
    return render(request, 'Web_App/index.html', context)

def stadions (request):
    context = {"stadions_page": "active"}
    return render(request, 'Web_App/stadions.html', context)
def faq (request):
    context = {"faq_page": "active"}
    return render(request, 'Web_App/faq.html', context)

def cennik (request):
    context = {"cennik_page": "active"}
    return render(request, 'Web_App/cennik.html', context)

def objednavka (request):
    context = {"objednavka_page": "active"}
    return render(request, 'Web_App/objednavka.html', context)

def kontakt (request):
    context = {"kontakt_page": "active"}
    return render(request, 'Web_App/kontakt.html', context)
    