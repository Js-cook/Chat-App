from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MessageSerializer
from .models import Message

# Create your views here.
@api_view(["GET"])
def api_overview(request):
  api_urls = {
    'List': '/api_list/',
    'Create': '/message_create',
    'Delete': '/message_delete/<str:pk>/',
  }
  return Response(api_urls)

@api_view(["GET"])
def api_list(request):
  messages = Message.objects.all()
  serializer = MessageSerializer(messages, many=True)
  
  return Response(serializer.data)

@api_view(["POST"])
def create_message(request):
  serializer = MessageSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(["DELETE"])
def delete_message(request):
  pass