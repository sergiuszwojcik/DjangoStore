import os
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.urls import reverse
from django.db.models import Q


# Generate name for uploaded images from product slugify(product.title)
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = slugify(instance.title)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    # final_filename = f'{new_filename}{ext}'
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


# Create your models here.

# With this we can query our own objects (using all(), filter())
class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True, active=True)

    def active(self):
        return self.filter(active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) |  # | or another things searching for Q(description__icontains=q)
                   # Reverse relation to ProductTag model. Returning products by tag title
                   Q(producttag__title__icontains=query))
        return self.filter(lookups).distinct()


class ProductManager(models.Manager):
    def all(self):
        return self.get_queryset().active()

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    # Product.objects.featured() instead of appending featured() at the end of query
    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        # Product.objects self.get_queryset()
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            # individual instance object
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=15, default=0.00)
    # null = True (can be null in database)
    # blank = True (can be null in django)
    # upload to media/products/ because there is MEDIA_URL added in settings
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def get_absolute_url(self):
        # return "/products/{slug}".format(slug=self.slug)
        return reverse('products:detail', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


# To generate slug befeore django model saves we need to make signal
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    # if instance doesn't have slug it will automatically generate slug
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
