"""pages_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# pages_project/urls.py
from django.contrib import admin
from django.contrib.auth import views as av
from django.urls import path, include
from users import views as u_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('register/', u_views.register, name='register'),
    path('change_password/', u_views.change_password, name='change_password'),
    path('profile/', u_views.profile, name='profile'),
    path('login/', av.LoginView.as_view(template_name='users/login.html'),
         name='login')
]
