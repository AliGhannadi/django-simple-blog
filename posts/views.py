from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Post, Tag, Category
def blog_home(request):
    posts = Post.objects.filter(status=1, created_date__lte=timezone.now()).order_by('-created_date')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'posts/blog.html', {
        'posts': posts, 
        'tags': tags,
        'categories': categories    
    })
def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tag=tag, status=1).order_by('-created_date')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'posts/blog.html', {
        'posts': posts,
        'current_tag': tag,
        'tags': tags,
        'categories': categories
        
    })
    
def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category, status=1).order_by('-created_date')
    categories = Category.objects.all()
    return render(request, 'posts/blog.html', {
        'posts': posts,
        'current_category': category,
        'categories': categories       
        
    })
    
def single_post(request, pid):
    post = get_object_or_404(Post, id=pid)
    categories = Category.objects.all
    return render(request, 'posts/single.html',{
        'post': post,
        'categories': categories,
        
    })