from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from staff.serializers import Profile_serializer, Products_Admin_serializer, Brands_Admin_serializer, Categories_Admin_serializer
from staff.serializers import Profile_write_serializer, Products_write_serializer
from rest_framework.views import APIView
from staff.models import Products
from customer.serializers import Product_serializers
from customer.models import Profile
from rest_framework.permissions import IsAdminUser
from rest_framework import status


class Profile_Admin_API(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request):
        data=Profile.objects.all()
        serial=Profile_serializer(data, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial=Profile_write_serializer(data=request.data)
        if serial.is_valid():
            profile=serial.save()
            return Response(Profile_serializer(profile).data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Profile_individual_API(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request, slug):
        data=get_object_or_404(Profile, slug=slug)
        serial=Profile_serializer(data)
        return Response(serial.data)
    
    def put(self, request, slug):
        data_ind=get_object_or_404(Profile, slug=slug)
        serial=Profile_write_serializer(data_ind, data=request.data, partial=True)
        if serial.is_valid():
            profile=serial.save()
            return Response(Profile_serializer(profile).data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, slug):
        data_ind=get_object_or_404(Profile, slug=slug)
        data_ind.delete()
        return Response({ 'message':'data is successfully deleted' })
    

class Products_Admin_view(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request):
        data=Products.objects.all()
        serial=Products_Admin_serializer(data, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial=Products_write_serializer(data=request.data)
        if serial.is_valid():
            product=serial.save()
            return Response(Products_Admin_serializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class Product_Admin_individual(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request, slug):
        data=get_object_or_404(Products, slug=slug)
        serial=Products_Admin_serializer(data)
        return Response(serial.data)
    
    def put(self, request, slug):
        data_ind=get_object_or_404(Products, slug=slug)
        serial=Products_write_serializer(data_ind, data=request.data, partial=True)
        if serial.is_valid():
            product=serial.save()
            return Response(Products_Admin_serializer(product).data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data=get_object_or_404(Products, slug=slug)
        data.delete()
        return Response({ 'message':'the product is deleted successfully.' })
