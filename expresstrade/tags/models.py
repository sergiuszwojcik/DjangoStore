from django.db import models
from django.db.models.signals import pre_save, post_save
from products.utils import unique_slug_generator
from django.urls import reverse
from products.models import Product


# Create your models here.

class ProductTag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    # Foreign key relation to Product model
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title


# To generate slug befeore django model saves we need to make signal
def product_tag_pre_save_receiver(sender, instance, *args, **kwargs):
    # if instance doesn't have slug it will automatically generate slug
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_tag_pre_save_receiver, sender=ProductTag)
