# pages/views.py
# from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def home(request):
    # return HttpResponse('<h1>test</h1>')
    

    return render(request, 'home.html', {'title': 'Home'} )

def about(request):
    return render(request, 'about.html', {'title':'About'})

def browse(request):
    return render(request, 'browse.html', {'title':'Browse'})
