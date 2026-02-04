from django import template
from ..models import Comment, Post

register = template.Library()

@register.inclusion_tag('blog/partials/sidebar/latest_posts.html')
def show_latest_posts():
    posts = Post.objects.all().order_by('-id')[:3]
    return {'posts': posts}



@register.inclusion_tag('blog/partials/sidebar/recent_comments.html')
def show_recent_comments(count=3):
    comments = Comment.objects.filter(is_active=1).order_by('-created_at')[:3]
    return {'comments': comments}
