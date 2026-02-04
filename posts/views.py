from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Post, Tag, Category, ContactMessage
from .forms import ContactForm, CommentForm
def blog_home(request):
    posts = Post.objects.filter(status=1, created_date__lte=timezone.now()).order_by('-created_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    tags = Tag.objects.all()
    categories = Category.objects.annotate(
        post_count=Count('posts', distinct=True)   
    )
    return render(request, 'blog/blog.html', {
        'posts': page_obj, 
        'tags': tags,
        'categories': categories    
    })
def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tag=tag, status=1).order_by('-created_date')
    tags = Tag.objects.all()
    categories = Category.objects.annotate(
        post_count=Count('posts', distinct=True)   
    )
    return render(request, 'blog/blog.html', {
        'posts': posts,
        'current_tag': tag,
        'tags': tags,
        'categories': categories
        
    })
    
def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category, status=1).order_by('-created_date')
    categories = Category.objects.annotate(
        post_count=Count('posts', distinct=True)   
    )
    return render(request, 'blog/blog.html', {
        'posts': posts,
        'current_category': category,
        'categories': categories       
        
    })
    
def single_post(request, pid):
    post = get_object_or_404(Post, id=pid)
    post.counted_views += 1
    post.save()
    tags = Tag.objects.all()
    categories = Category.objects.annotate(
        post_count=Count('posts', distinct=True)   
    )
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user_comment = request.user
            comment.save()
            messages.add_message(request,messages.SUCCESS,'Your comment has been submitted. It will appear after the admin confirmation.')
            return redirect('blog:single', post.id)
        else:
            messages.add_message(request,messages.ERROR,'Your comment has not been submitted.')
    else:
     form = CommentForm()
    
    active_comments = post.comments.filter(is_active=True)    
    return render(request, 'blog/single.html',{
        'post': post,
        'categories': categories,
        'form': form,
        'comment_count': active_comments.count(),
        'tags': tags,
        
    })
    
def blog_search(request):
    posts = Post.objects.filter(status=1, created_date__lte=timezone.now())
    if s := request.GET.get('s'):
        posts = posts.filter(
            Q(title__icontains=s) |
            Q(content__icontains=s)
            
        )
    categories = Category.objects.annotate(
        post_count=Count('posts', distinct=True)
    )
    tags = Tag.objects.all()
    return render(request, 'blog/blog.html', {
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'search_query': request.GET.get('s', '')
    })
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your message has been sent. We will contact you via email as soon as possible.')
        else:
            messages.add_message(request,messages.ERROR, 'Failed to sent message')
    
    form = ContactForm()
    return render(request, 'contact.html', {"form": form})
