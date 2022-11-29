from django.shortcuts import redirect, render
from django.views import View
from category.models import *

from product.models import *
from django.core.paginator import Paginator



# Create your views here.
class Detail(View):
    def get(self, re, p, c, s):
        pr = Product.objects.get(id=p)
        if Product.objects.get(id=p).chegirma_true==True:
            chegirma = Product.objects.get(id=p).price - Product.objects.get(id=p).chegirma
        else:
            chegirma = False
        data = {
            'comments': Comment.objects.filter(product=pr),
            'product' : pr,
            "subname" : Subcategory.objects.get(id=s).name,
            'catname' : Category.objects.get(id=c).name,
            "chegirma" : chegirma,
        }

        return render(re, "page-detail-product.html", data)

    def post(self, re, p, c, s):
        pr = Product.objects.get(id=p)
        text = re.POST['comment-text']
        Comment.objects.create(text=text, product=pr, user=re.user)
        return redirect(f"/1/1/{p}/")

def listing(request):
    p = Paginator(Product.objects.all(), 1)
    page = request.GET.get('page')
    pages =p.get_page(page)
    data = {
        'pages': pages,
        'products': Product.objects.all(),
    }
    return render(request, "page-listing-grid.html", data)
