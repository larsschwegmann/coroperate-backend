from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from requests.models import Request
from requests.serializers import RequestSerializer, UserSerializer

# Create your views here.
class RequestListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
