from django.contrib import admin
from .models import *

admin.site.register(Products)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Basket)