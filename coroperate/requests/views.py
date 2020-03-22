from django.contrib.auth.models import User
from rest_framework import generics
from requests.models import Request
from requests.serializers import RequestSerializer, UserSerializer

# Create your views here.
class RequestListCreate(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
