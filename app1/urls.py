from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('saludo/', views.presentacion),


]



#se creo este archivo agregando nuevas urls

#git init
#git add . 
#git commit -m ""
#git remote add origin 'se agrega el url'
#git config --global user.name DaniloAbarzua  
# git config --global user.email danilo.abarzua@inacapmail.cl
#  