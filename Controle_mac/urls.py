"""Controle_mac URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse('Bem Vindo a pagina home')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("cadastro/", include("Controle_mac.Apps.Cadastro.urls")),
    path("supervisor/", include("Controle_mac.Apps.Supervisor.urls")),
    path("tecnico/", include("Controle_mac.Apps.Tecnico.urls")),
]
