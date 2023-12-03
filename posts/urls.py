from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='posts-index' ),
    path('posts', views.postsList, name='posts-list' ),
    path('post', views.post, name='post' ),
]