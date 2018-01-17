from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar/', views.buscar, name='buscar'),

    path('api/<slug:table>/', views.lista, name='lista'),
    path('api/<slug:table>/<slug:id>', views.modelo, name='valor'),
]
