from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=False, null=False, default="09916716575")
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    def __str__(self):
        return self.username
    