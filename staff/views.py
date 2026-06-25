from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from staff.serializers import Profile_serializer, Products_Admin_serializer, Brands_Admin_serializer, Categories_Admin_serializer
from rest_framework.views import APIView
from staff.models import Products
from customer.serializers import Product_serializers
from customer.models import Profile
from rest_framework.permissions import IsAdminUser


class Profile_Admin_API(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request):
        data=Profile.objects.all()
        serial=Profile_serializer(data, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial=Profile_serializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        
class Profile_individual_API(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request, slug):
        data=get_object_or_404(Profile, slug=slug)
        serial=Profile_serializer(data)
        return Response(serial.data)
    
    def put(self, request, slug):
        data_ind=get_object_or_404(Profile, slug=slug)
        serial=Profile_serializer(data_ind, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
    
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
        serial=Products_Admin_serializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)

class Product_Admin_individual(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request, slug):
        data=get_object_or_404(Products, slug=slug)
        serial=Products_Admin_serializer(data)
        return Response(serial.data)
    
    def put(self, request, slug):
        data_ind=get_object_or_404(Products, slug=slug)
        serial=Products_Admin_serializer(data_ind, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)

    def delete(self, request, slug):
        data=get_object_or_404(Products, slug=slug)
        data.delete()
        return Response({ 'message':'the product is deleted successfully.' })