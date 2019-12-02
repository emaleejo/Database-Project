# pages/urls.py
from django.urls import path

# from .views import HomePageView, AboutPageView, SearchPageView # new
from . import views
from .views import BookListView, BookDetailView

urlpatterns = [
    path('', views.home, name='pages-home'),
    path('about/', views.about, name='pages-about'), # new
    path('browse/', views.browse, name='pages-browse'),
    path('order/', views.order, name='order'),
    path('remove/<int:pk>', views.delete_from_cart, name='remove'),
    path('browse/<int:pk>/', BookDetailView.as_view(), name='pages-detail'),
    # path('browse/<int:pk>/new/', ReviewCreateView.as_view(), name='book-review'),
    path('cart/<int:isbn>', views.add_to_cart, name='pages-add'),
]   