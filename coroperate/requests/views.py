from django.shortcuts import render
from rest_framework import generics
from requests.models import Request
from requests.serializers import RequestSerializer

# Create your views here.
class RequestList(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
