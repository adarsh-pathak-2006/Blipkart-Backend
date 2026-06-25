from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from staff.models import Products
from customer.models import Cart, Profile
from customer.serializers import Product_serializers, Cart_serializers, Profile_serializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class HomeView(APIView):
    def get(self, request):
        data=Products.objects.filter(isactive=True)
        serial=Product_serializers(data, many=True)
        return Response(serial.data)

class IndividualProductView(APIView):
    def get(self, request, slug):
        data=get_object_or_404(Products, slug=slug)
        serial=Product_serializers(data)
        return Response(serial.data)

class CartView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        profile_data=Profile.objects.get(user=request.user)
        data=Cart.objects.filter(profile=profile_data)
        serial=Cart_serializers(data, many=True)
        return Response(serial.data)

    
    def post(self, request):
        cart_data=Cart_serializers(data=request.data)
        if cart_data.is_valid():
            user_data=Profile.objects.get(user=request.user)
            cart_data.save(profile=user_data)
            return Response(cart_data.data)
            

class ProfileView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        data=Profile.objects.get(user=request.user)
        serial=Profile_serializer(data)
        return Response(serial.data)
    
    def put(self, request):
        instance=Profile.objects.get(user=request.user)
        serial=Profile_serializer(instance, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
    
