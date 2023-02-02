from django.contrib import admin

from products.models import Category, ProductImage, Products

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(ProductImage)

