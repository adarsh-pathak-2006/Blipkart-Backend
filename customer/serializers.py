from rest_framework.serializers import ModelSerializer
from staff.models import Products, Category, Brands
from customer.models import Profile, Cart
from whoisthis.serializers import User_serializer

class Category_serializer(ModelSerializer):
    class Meta:
        model=Category
        fields=['name', 'description']


class Brands_serializer(ModelSerializer):
    class Meta:
        model=Brands
        fields=['name']

class Profile_serializer(ModelSerializer):
    user=User_serializer()
    class Meta:
        model=Profile
        fields=['user', 'address', 'phoneNo', 'date_joined']   


class Product_serializers(ModelSerializer):
    category=Category_serializer()
    brand=Brands_serializer()
    class Meta:
        model=Products
        fields=['name', 'description', 'price', 'stock', 'category', 'brand', 'created_date', 'isactive']


class Cart_serializers(ModelSerializer):
    product=Product_serializers()
    profile=Profile_serializer()
    class Meta:
        model=Cart
        fields=['product', 'added_on', 'profile', 'quantity']
