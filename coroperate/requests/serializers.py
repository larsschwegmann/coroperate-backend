from rest_framework import serializers
from requests.models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request