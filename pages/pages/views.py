# pages/views.py
# from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Book, Author, Category, Order, OrderItem
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import decimal as decimal

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
    item = Book.objects.filter(isbn=isbn).first()
    price = decimal.Decimal(item.price)
    order, created = Order.objects.get_or_create(user=request.user,Order_Value=0)
    orderitem, created = OrderItem.objects.get_or_create(item=item, Item_Price=0, order=order)
    order.items.add(orderitem)
    order.save()
    messages.success(request, 'Cart Updated!')
    return redirect('pages-browse')

@login_required
def delete_from_cart(request, pk):
    item_to_delete = OrderItem.objects.filter(ItemNumber=pk)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect('order')



class BookListView(ListView):
    model = Book
    template_name = 'browse.html'
    context_object_name = 'books'
    ordering = ['title']

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class ReviewCreateView(CreateView):
    # model = Review
    template_name = 'review.html'
    fields = ["title",'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

def order(request):
    o = Order.objects.filter(user=request.user)
    o = list(o.first().items.all())
    context={
        'title':'Order',
        'items':o
    }

    return render(request,'order_detail.html', context)

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

def complete(request):
    return render(request, 'complete.html', {'title':'Complete'})