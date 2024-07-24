from django.db import models
from django.utils import timezone

class Up_UsersDetails(models.Model):
    UserName = models.CharField(max_length=50)
    official_email = models.CharField(unique=True, max_length=100)
    primary_contact_number = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=255)
    profile_image = models.CharField(max_length=255, blank=True, null=True)
    web_auth_token = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
   
    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.official_email
