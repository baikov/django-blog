from django.contrib import admin

from .models import Post, PostImages


class PostImagesInline(admin.TabularInline):
    model = PostImages
    extra = 3
# class PostAdmin(admin.ModelAdmin):


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'slug', 'is_highlighted', 'is_published')
    list_filter = ['created_date']
    search_fields = ['title']
    inlines = [PostImagesInline, ]
    fieldsets = [
        (None, {'fields': ['is_published', 'title', 'is_highlighted', 'is_toc', 'toc_depth', 'short_text', 'image', 'body']}),
        ('SEO', {'fields': ['slug', 'seo_title', 'seo_description']}),
    ]


admin.site.register(Post, PostAdmin)
