from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    prepopulated_fields = {"slug": ("name",)}
    class Meta:
      verbose_name_plural = "Categories"
    def __str__(self):
      return  self.name
class Post(models.Model):
    # img
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.title}"
    
    category = models.ManyToManyField(
        Category,
        related_name="posts",
        blank=True
    )
    # tag
    
