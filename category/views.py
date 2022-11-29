from django.shortcuts import render

from .models import *

# Create your views here.
def category(r):
    return render(r, "page-category.html", {'categories': Category.objects.all(), "subcategories": Subcategory.objects.all()})
