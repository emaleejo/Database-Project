# pages/views.py
# from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Book, Author, Category, Order, OrderItem
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required
def add_to_cart(request, isbn):
    isbn = request.POST.get('isbn')
    item = Book.objects.filter(isbn=isbn).first()
    order, created = Order.objects.get_or_create(user=request.user)
    orderitem, created = OrderItem.objects.get_or_create(book=item, order=order)
    order.save()
    messages.success(request, 'Cart Updated!')
    return redirect('pages-browse')

class BookListView(ListView):
    model = Book
    template_name = 'browse.html'
    context_object_name = 'books'
    ordering = ['title']

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

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

