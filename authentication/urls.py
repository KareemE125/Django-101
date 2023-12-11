from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('logout', views.logoutPage, name='logout'),
]