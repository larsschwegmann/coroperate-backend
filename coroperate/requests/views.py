from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from requests.models import Request
from requests.serializers import RequestSerializer, UserSerializer

# Create your views here.
class RequestListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Request.objects.filter(zip_code=user.profile.zip_code)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
