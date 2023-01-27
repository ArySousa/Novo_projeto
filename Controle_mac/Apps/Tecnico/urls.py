from django.urls import path
from Controle_mac.Apps.Tecnico.views import tecnico,  novo, editar, excluir



urlpatterns = [
    path("", tecnico),
    path("novo/", novo),
    path("editar/", editar),
    path("excluir/", excluir),
]