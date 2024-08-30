from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('saludo/', views.presentacion),


]



#se creo este archivo agregando nuevas urls

 