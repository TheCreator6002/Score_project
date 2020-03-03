from django.contrib import admin
from .models import Category, Manufacturer, Product, Reviews

admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(Reviews)


