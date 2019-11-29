# pages/urls.py
from django.urls import path

# from .views import HomePageView, AboutPageView, SearchPageView # new
from . import views

urlpatterns = [
    # path('search/', name='search'), # new
    path('', views.home, name='pages-home'),
    path('about/', views.about, name='pages-about'), # new
    path('browse/', views.browse, name='pages-browse'),
]