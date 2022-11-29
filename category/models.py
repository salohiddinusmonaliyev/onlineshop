from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=70)
    image = models.FileField(upload_to="category/", null=True)
    recommended = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to="subcategory/", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name