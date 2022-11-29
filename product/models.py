from django.db import models

from django.contrib.auth.models import User


from category.models import *

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    price = models.IntegerField()
    image = models.FileField(upload_to="products/")
    unit = models.CharField(max_length=40)
    guarantee = models.SmallIntegerField()
    delivery = models.SmallIntegerField()
    availabilty = models.CharField(max_length=40)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    chegirma_true = models.BooleanField()
    chegirma = models.IntegerField(null=True, blank=True)
    recommended = models.BooleanField()
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    review = models.IntegerField(default=5, null=True)

    def __str__(self):
        return self.product.title
