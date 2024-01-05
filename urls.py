# this urls.py file is of App
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('done/<int:pk>/', views.delete, name='delete'),
]
