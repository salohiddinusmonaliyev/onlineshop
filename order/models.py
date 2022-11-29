from django.db import models
from accounts.models import Account
from product.models import *

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title