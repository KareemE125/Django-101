from django.urls import path
from . import views

urlpatterns = [
    path('', views.postsList, name='posts' ),
    path('add', views.addPost, name='add-post' ),
    path('<str:id>', views.post, name='post' ),
    path('<str:id>/edit', views.editPost, name='edit-post' ),
    path('<str:id>/delete', views.deletePost, name='delete-post' ),
]