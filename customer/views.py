from django.shortcuts import render
from rest_framework.views import APIView
from staff.models import Products
from customer.models import Cart, Profile
from customer.serializers import Product_serializers, Cart_serializers
from rest_framework.response import Response

class HomeView(APIView):
    def get(self, request):
        data=Products.objects.all()
        serial=Product_serializers(data, many=True)
        return Response(serial.data)
    

class CartView(APIView):
    def get(self, request):
        profile_data=Profile.objects.filter(user=request.user)
        data=Cart.objects.filter(profile=profile_data)
        serial=Cart_serializers(data, many=True)
        return Response(serial.data)

class ProfileView(APIView):
    def get(self, request):
        