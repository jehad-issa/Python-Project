from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page),
    path('login',views.login_page),
    path('register',views.register),
    path('loginproccese',views.login_proccese)
]
