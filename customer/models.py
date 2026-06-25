from django.db import models
from django.contrib.auth.models import User
from staff.models import Products

class Address(models.Model):
    home_address=models.CharField(max_length=300, null=True)
    work_address=models.CharField(max_length=300, null=True)


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.OneToOneField(Address, on_delete=models.CASCADE)
    phoneNo=models.CharField(max_length=15)
    date_joined=models.DateField(auto_now_add=True)
    slug=models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.user.first_name


class Cart(models.Model):
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return self.product.name




