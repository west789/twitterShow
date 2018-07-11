from django.urls import path
from . import views

urlpatterns = [
    path('index/<int:value1>/<int:value2>/', views.index),
]