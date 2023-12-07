from django.contrib import admin
from .models import Post, Author

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'images', 'category', 'isDeleted', 'createdAt']
    list_display_links = ['title']
    list_editable = [ 'category']
    search_fields = ['title']
    list_filter = ['author', 'isDeleted', 'category']
    
admin.site.register(Post, PostAdmin)
admin.site.register(Author)