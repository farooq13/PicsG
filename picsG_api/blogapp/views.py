from django.shortcuts import render
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
 

def register_user(request):
  serializer = UserRegistrationSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 