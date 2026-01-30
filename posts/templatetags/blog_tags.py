from django import template
from ..models import Post


register = template.Library()

@register.inclusion_tag('posts/partials/sidebar/latest_posts.html')
def show_latest_posts(count=3):
    posts = Post.objects.all().order_by('-id')[:count]
    return {'posts': posts}
