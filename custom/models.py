from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

class Order(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='order', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    NAME_CHOICES = [
        ('Laptop', 'Laptop'),
        ('Mobile', 'Mobile'),
        ('Tablet', 'Tablet'),
        ('Headphones', 'Headphones'),
        ('Smartwatch', 'Smartwatch'),
    ]

    name = models.CharField(
        max_length=255,
        unique=True,
        choices=NAME_CHOICES,  # Dropdown with predefined options
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Auto-generate slug from name
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name