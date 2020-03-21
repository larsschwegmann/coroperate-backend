from django.shortcuts import render
from rest_framework import generics
from requests.serializers import RequestSerializer, ShoppingItemSerializer
from requests.models import Request, ShoppingItem


class RequestList(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class ShoppingItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer

