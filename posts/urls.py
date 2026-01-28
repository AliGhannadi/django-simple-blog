from django.urls import path
from .views import blog_home, post_by_tag, post_by_category
app_name = 'posts'
urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('tag/<slug:tag_slug>/', post_by_tag, name='tag'),
    path('category/<slug:category_slug>', post_by_category, name='cat')
    
]
