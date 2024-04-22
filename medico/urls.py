from django.urls import path
from . import views

urlpatterns = [
    path("cadastro_medico/", views.cadastro_medico, name="cadastro_medico"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.sair, name="sair"),
]
