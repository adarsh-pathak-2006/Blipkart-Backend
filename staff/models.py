from django.db import models


class Category(models.Model):
    name=models.CharField()
    description=models.TextField()

    def __str__(self):
        return self.name


class Brands(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Products(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.IntegerField()
    stock=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    brand=models.ForeignKey(Brands, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    isactive=models.BooleanField(default=False)


    def __str__(self):
        return self.name

