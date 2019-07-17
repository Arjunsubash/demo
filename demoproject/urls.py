from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.Login, name='Login'),
    path('home/', views.Home, name='Home'),
]