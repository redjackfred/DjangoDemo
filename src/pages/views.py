from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello Django</h1>")

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Me</h1>")

def about_view(*args, **kwargs):
    return HttpResponse("<h1>About Me Page</h1>")

def social_view(*args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")