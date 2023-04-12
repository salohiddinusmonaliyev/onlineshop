from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.FileField(upload_to="profile/", null=True, default=None)
    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    ph_num = models.CharField(max_length=40, null=True, default=None)
    gender = models.CharField(max_length=50, choices=GENDER)

    class Meta:
        verbose_name = ("Account")
        verbose_name_plural = ("Accounts")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
