from django.conf.urls import url
#para importar vista basadas en clases
from .views import LoginView, RegisterView
#para importa vistas basadas en funciones
from . import views

urlpatterns = [
    url(r'^ingresar/$', LoginView.as_view(), name="login"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^salir/$', views.LogOut, name="logout"),
]