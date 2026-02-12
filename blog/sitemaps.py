from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'
    
    def items(self):
        return ['blog:blog_home', 'blog:contact', 'accounts:profile']
    def location(self, item):
        return reverse(item)
    
    
class BlogSiteMap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    def items(self):
        return Post.objects.filter(status=True)
    def location(self, item):
        return reverse(item)