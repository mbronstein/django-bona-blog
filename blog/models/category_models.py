# Core Django imports.
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from categories.base import CategoryBase


class Category(CategoryBase):

    image = models.ImageField(default='category-default.jpg',
                              upload_to='category_images')
    approved = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('blog:category_articles',
                       kwargs={'slug': self.slug})
