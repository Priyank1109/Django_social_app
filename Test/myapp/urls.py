from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/',index,name = "login"),
    path('register/',register, name = "register"),
    path('lists/',lists, name = "lists"),
    path('update_user/',update_user, name = "update_user"),
    path('delete_user/',delete_user, name = "delete_user"),
    path('', post_list, name='post_list'),
    path('logout/', custom_logout, name='logout'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('like/<int:pk>/', like_post, name='like_post'),
    path('post/', post_create_view, name='post_create'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)