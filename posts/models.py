from django.db import models
from django.utils import timezone
from django.conf import settings
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    def __str__(self):
       return self.name
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    class Meta:
      verbose_name_plural = "Categories"
    def __str__(self):
      return  self.name
class Post(models.Model):
    img = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
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
    tag = models.ManyToManyField(
        Tag,
        related_name="posts",
        blank=True
    )
    counted_views = models.IntegerField(default=0)
    
    @property
    def active_comment_count(self):
        return self.comments.filter(is_active=1).count()
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return f"{self.name} - {self.subject}"
   

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user_comment = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_comment"
    )
    content = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)