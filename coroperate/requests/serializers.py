from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from requests.models import Request, Item, Profile


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item']


class RequestSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    items = ItemSerializer(many=True)

    class Meta:
        model = Request
        fields = ['id', 'items', 'owner', 'address', 'zip_code', 'city', 'tip', 'date', 'acceptor']

    def create(self, validated_data):
        """
        Custom create method to create request and corresponding items in one go.
        """
        validated_item_data = validated_data.pop('items')
        request = Request.objects.create(**validated_data)
        item_serializer = self.fields['items']
        for item in validated_item_data:
            item['request'] = request
        item_serializer.create(validated_item_data)
        return request

    def update(self, instance, validated_data):
        """
        Custom update method to create request and corresponding items in one go.
        """
        instance.save()
        return instance()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['address', 'zip_code', 'city']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['id', 'profile', 'username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        validated_profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        profile_serializer = self.fields['profile']
        validated_profile_data['user'] = user
        profile_serializer.create(validated_profile_data)
        return user

    def validate_password(self, password):
        return make_password(password)
