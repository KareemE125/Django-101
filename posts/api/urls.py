from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('posts', views.getPosts),
    path('posts/<int:id>', views.getPost),
]
