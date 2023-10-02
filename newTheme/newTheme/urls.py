"""
URL configuration for newTheme project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from app3.views import param_func
import theme.views
from theme.views import lst_genres_jazz, main_page

urlpatterns = [
    # 127.0.0.1:8000/
    path("", main_page),
    path('templates/genres.html/', include("theme.urls")),
    path('templates/genres.html/', lst_genres_jazz),
    # path('pop/'),
    # path('classic/'),

    path('admin/', admin.site.urls),
]
