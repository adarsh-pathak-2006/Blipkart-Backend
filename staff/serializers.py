from rest_framework.serializers import ModelSerializer
from customer.models import Profile
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




