from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    price = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='product_main_image', blank=True, null=True)


    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image')

    def __str__(self):
        return self.product.name


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    # image = models.ImageField(upload_to='category_icons', blank=True, null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
