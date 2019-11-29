# pages/urls.py
from django.urls import path

from .views import HomePageView, AboutPageView, SearchPageView # new
from . import views

urlpatterns = [
    path('search/', SearchPageView.as_view(), name='search'), # new
    path('about/', AboutPageView.as_view(), name='about'), # new
    path('', HomePageView.as_view(), name='home'),  
    path('', views.index, name='index'),
]