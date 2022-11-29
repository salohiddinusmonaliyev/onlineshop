from django.shortcuts import redirect, render
from category.models import *

from product.models import Product


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        data = {
            'products' : Product.objects.filter(recommended = True),
            "category" : Category.objects.filter(recommended = True),
            "subcategory" : Subcategory.objects.all(),
        }
        return render(request, "page-index-1.html", data)
    return redirect('/login/')
