from django.contrib import admin
from django.urls import path
from .view import index

urlpatterns = [
    path('/', index, name='index'),
]
