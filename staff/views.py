from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import User_serializers
from rest_framework.views import APIView


class User_API(APIView):
    def get(self, request):
        user_data=User.objects.all()
        serial=User_serializers(user_data, many=True)
        return Response(serial.data)

    def post(self, request):
        serial=User_serializers(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)

class UserIndividual_API(APIView):
    def get(self, request, pk):
        data=get_object_or_404(User, id=pk)
        serial=User_serializers(data)
        return Response(serial.data)
    
    def put(self, request, pk):
        user_data=get_object_or_404(User, id=pk)
        serial=User_serializers(user_data, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        
    def delete(self, request, pk):
        user=get_object_or_404(User, id=pk)
        user.delete()
        return Response({ 'message':'user is deleted successfully' })

