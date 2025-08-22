from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Home Page of Ebooks Library")

def about(request):
    return HttpResponse("About Page of Ebooks Library")

def social_media(request):
    return HttpResponse("Social Media Page of Ebooks Library")

def contacts(request):
    return HttpResponse("contacts Page of Ebooks Library")
