from django.db.models.signals import pre_save
from django.dispatch import receiver

from .utils import custom_slugify
from .models import Post

@receiver(pre_save, sender=Post)
def pre_save_slugify(sender, instance, **kwargs):
    instance.slug = custom_slugify(sender, instance.title)