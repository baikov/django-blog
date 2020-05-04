from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'slug')
    list_filter = ['created_date']
    search_fields = ['title']
    fieldsets = [
        (None, {'fields': ['title', 'short_text', 'image', 'body']}),
        ('SEO', {'fields': ['slug', 'seo_title', 'seo_description']}),
    ]

admin.site.register(Post, PostAdmin)