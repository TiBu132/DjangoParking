from django.urls import path
from rest_estacionamiento.views import UserView, RegisterView
urlpatterns = [
    path('users/', UserView.as_view()),
    path('register', RegisterView.as_view()),
]