# pages/views.py
from django.views.generic import TemplateView
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class HomePageView(TemplateView):
    template_name = 'home.html'
class AboutPageView(TemplateView): # new
    template_name = 'about.html'

class SearchPageView(TemplateView): # new
    template_name = 'search.html'