from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', "availabilty")
    prepopulated_fields = {"slug": ("title", )}

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
