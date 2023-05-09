from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="logpage"),
    path("about/", views.about, name="Aboutus"),
    path("Cars/<int:carid>", views.carview, name="carView"),
    path("contact/", views.contact, name="contactus"),
    path("signup/", views.handleSignUp, name="handleSignUp"),
    path('login/', views.handeLogin, name="handleLogin"),
    path('logout/', views.handelLogout, name="handleLogout"),
]
   





