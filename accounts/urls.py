from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('login/', views.loginPage, name="login"),
    path('registr/', views.registrPage, name="registr"),
    path('logout/', views.logoutUser, name="logout"),
]