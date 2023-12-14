from django.urls import path
from rest_estacionamiento.views import UserView, RegisterView, EstacionamientoView, VehiculoView
urlpatterns = [
    path('users/', UserView.as_view()),
    path('register', RegisterView.as_view()),
    path('estacionamiento', EstacionamientoView.as_view()),
    path('vehiculo', VehiculoView.as_view())
]