"""Tradutor URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from app.publicacao.views import *
from app.publicacao.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='url_login'),
    path('feed', feed, name='url_feed'),
    path('publicar/<int:pk>', publicar, name='url_publicar'),
    path('profile/<int:pk>', profile, name='url_profile'),
    path('deletar/<int:pk>', delete, name='url_delete'),
    path('logout', logout_view, name='url_logout'),
    path('cadastro/', RegisterView.as_view(), name='url_cadastro'),
    path('comentar/<int:pk>', comentar, name='url_comentario'),
    path('comentarios/<int:pk>', comentarios, name='url_comentarios'),
    
]

