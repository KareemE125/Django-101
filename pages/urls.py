from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='pages-default' ),
    path('index/', views.index, name='pages-index' ),
]