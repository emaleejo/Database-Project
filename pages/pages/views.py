# pages/views.py
# from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, Category
from django.db.models import Q
from django import forms

def home(request):
    # return HttpResponse('<h1>test</h1>')
    

    return render(request, 'home.html', {'title': 'Home'} )

def about(request):
    return render(request, 'about.html', {'title':'About'})

class SearchForm(forms.Form):
    choices = [
        ('Book Title', 'Book Title'),
        ('ISBN', 'ISBN'),
        ('Author','author'),
        ('Category','category'),
    ]
    choice = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)


def browse(request):
    form = SearchForm

    context = {'form':form}
    query = ""
    if request.GET:
        
        query = request.GET['q']
        context['query'] = str(query)


    context = {
        'title':'Browse',
        'books':get_queryset(query),
        'form':form
    }
    return render(request, 'browse.html', context)

def get_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        results = Book.objects.filter(
            Q(title__icontains=q) |
            Q(isbn__icontains=q)
        ).distinct()
    for b in results:
        queryset.append(b)

    return list(set(queryset))