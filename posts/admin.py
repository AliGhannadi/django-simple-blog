from django.contrib import admin
from .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_date')
    list_filter = ('status', 'created_date')
    search_fields = ('title', 'content')
    

admin.site.register(Category)