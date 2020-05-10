from django.db import models
from django.urls import reverse


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(is_published=True)

    def featured(self):
        return self.filter(is_highlighted=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    short_text = models.TextField(
        max_length=250, verbose_name='Short Text', blank=True)
    image = models.ImageField(blank=True)
    seo_title = models.CharField(max_length=200, blank=True)
    seo_description = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(blank=True)
    body = models.TextField()
    is_published = models.BooleanField(verbose_name='Published', default=False, null=False)
    is_highlighted = models.BooleanField(verbose_name='Featured', default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})
