from django.contrib import admin
from .models import Post, Category, ContactMessage, Comment
from .models import Tag
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_date')
    list_filter = ('status', 'created_date')
    search_fields = ('title', 'content')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'subject', 'message')
    def has_add_permission(self, request):
        return False
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_comment', 'post', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('user_comment__username', 'content')
    actions = ['approve_comments']
    def approve_comments(self, request, queryset):
        queryset.update(is_active=True)