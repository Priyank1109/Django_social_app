from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Up_UsersDetails(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    username = models.CharField(max_length=150, unique=True,blank=True, null=True)
    email = models.CharField(unique=True, max_length=100)
    primary_contact_number = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=255)
    profile_image = models.CharField(max_length=255, blank=True, null=True)
    web_auth_token = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    last_login = models.DateTimeField(null=True)
    last_ip = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(default=1)
    is_distributor = models.IntegerField(default=0)
    is_super_stockist = models.IntegerField(default=0)
    is_retailer = models.IntegerField(default=0)
    is_tagged = models.IntegerField(default=0)
    is_superuser = models.IntegerField(default=1)
    is_staff = models.IntegerField(default=1)
    is_active = models.IntegerField(default=1)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
   
    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.email


class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Up_UsersDetails, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Up_UsersDetails, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(Up_UsersDetails, on_delete=models.CASCADE)
    
    

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
