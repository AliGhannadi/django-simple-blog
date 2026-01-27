from django.shortcuts import render
from django.utils import timezone
from .models import Post
def blog_home(request):
    posts = Post.objects.filter(status=1, created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'posts/blog.html', {'posts': posts})
