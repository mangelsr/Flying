from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('cargar_base/', views.cargar_base, name='cargarBase'),
    path('buscar/', views.buscar, name='buscar'),
]
