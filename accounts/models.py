from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class CustomUser(AbstractUser):
    # override email to make it unique and required
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    biography = models.TextField(default="No bio")
    def __str__(self):
        return self.username
    
    
    
    
