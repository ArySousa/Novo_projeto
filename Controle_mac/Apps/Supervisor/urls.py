from django.urls import path
from Controle_mac.Apps.Supervisor.views import supervisor,  novo, editar, excluir



urlpatterns = [
    path("", supervisor),
    path("novo/", novo),
    path("editar/", editar),
    path("excluir/", excluir),

]