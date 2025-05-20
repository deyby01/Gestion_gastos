from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index, name="index"),  # Ruta para la página principal
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("eliminar/<int:gasto_id>/", views.eliminar_gasto, name="eliminar_gasto"),
]