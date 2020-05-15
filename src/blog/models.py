import os
from django.db import models
from django.urls import reverse
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


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
    body = RichTextUploadingField()
    is_toc = models.BooleanField(verbose_name='TOC', default=False)
    toc_depth = models.PositiveSmallIntegerField(verbose_name='TOC depth', default=6)
    is_published = models.BooleanField(verbose_name='Published', default=False, null=False)
    is_highlighted = models.BooleanField(verbose_name='Featured', default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})


def get_image_filename(instance, filename):
    # ext = filename.split('.')[-1]
    if instance.post.slug:
        slug = instance.post.slug
    else:
        slug = instance.post.pk
    #     filename = f'{instance.post.slug}.{ext}'
    path = f'post-img/{slug}/'
    return os.path.join(path, filename)


class PostImages(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    img_alt = models.CharField(max_length=200, blank=True)
    img_title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image', blank=True)
