from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/',index,name = "login"),
    path('register/',register, name = "register"),
    path('lists/',lists, name = "lists"),
    path('update_user/',update_user, name = "update_user"),
    path('delete_user/',delete_user, name = "delete_user"),
    


    
]
