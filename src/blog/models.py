from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    short_text = models.TextField(max_length=250, verbose_name='Short Text', blank=True)
    image = models.ImageField(blank=True)
    seo_title = models.CharField(max_length=200, blank=True)
    seo_description = models.CharField(max_length=250, blank=True)
    slug = models.SlugField()
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
