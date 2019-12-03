# pages/urls.py
from django.urls import path

# from .views import HomePageView, AboutPageView, SearchPageView # new
from . import views
from .views import ReviewCreateView

urlpatterns = [
    path('', views.home, name='pages-home'),
    path('about/', views.about, name='pages-about'), # new
    path('browse/', views.browse, name='pages-browse'),
    path('order/', views.order, name='order'),
    path('remove/<int:pk>', views.delete_from_cart, name='remove'),
    path('browse/<int:pk>/', views.bookdetail, name='pages-detail'),
    path('browse/<int:pk>/new/', ReviewCreateView.as_view(),{'isbn':'<int:pk>'}, name='book-review'),
    path('cart/<int:isbn>', views.add_to_cart, name='pages-add'),
    path('complete/', views.complete, name='complete'),
]   