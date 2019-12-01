# pages/urls.py
from django.urls import path

# from .views import HomePageView, AboutPageView, SearchPageView # new
from . import views
from .views import BookListView, BookDetailView

urlpatterns = [
    
    path('', views.home, name='pages-home'),
    path('about/', views.about, name='pages-about'), # new
    path('browse/', BookListView.as_view(), name='pages-browse'),
    path('browse/<int:pk>/', BookDetailView.as_view(), name='pages-detail'),
    
]