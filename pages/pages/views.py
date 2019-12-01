# pages/views.py
# from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Book, Author, Category
from django.db.models import Q

def home(request):
    return render(request, 'home.html', {'title': 'Home'} )

def about(request):
    return render(request, 'about.html', {'title':'About'})

def browse(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    context = {
        'title':'Browse',
        'books':get_queryset(query),
    }
    return render(request, 'browse.html', context)

class BookListView(ListView):
    model = Book
    template_name = 'browse.html'
    context_object_name = 'books'

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

