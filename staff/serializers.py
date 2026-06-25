from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from django.contrib.auth.models import User
from customer.models import Profile, Address
from whoisthis.serializers import User_serializer
from staff.models import Products, Brands, Category

class Profile_serializer(ModelSerializer):
    user=User_serializer()
    class Meta:
        model=Profile
        fields='__all__'

class Categories_Admin_serializer(ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class Brands_Admin_serializer(ModelSerializer):
    class Meta:
        model=Brands
        fields='__all__'

class Products_Admin_serializer(ModelSerializer):
    category=Categories_Admin_serializer()
    class Meta:
        model=Products
        fields='__all__'


class Profile_write_serializer(ModelSerializer):
    user=PrimaryKeyRelatedField(queryset=User.objects.all())
    address=PrimaryKeyRelatedField(queryset=Address.objects.all(), allow_null=True, required=False)
    class Meta:
        model=Profile
        fields=['user', 'address', 'phoneNo', 'slug']


class Products_write_serializer(ModelSerializer):
    category=PrimaryKeyRelatedField(queryset=Category.objects.all())
    brand=PrimaryKeyRelatedField(queryset=Brands.objects.all())
    class Meta:
        model=Products
        fields=['name', 'description', 'price', 'stock', 'category', 'brand', 'isactive', 'slug']




