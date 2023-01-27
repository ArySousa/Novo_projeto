from django.urls import path
from Controle_mac.Apps.Cadastro.views import cadastro, novo, editar, excluir


urlpatterns = [
    path("", cadastro),
    path("novo/", novo),
    path("editar/", editar),
    path("excluir/", excluir),
]
