from rest_framework import serializers
from requests.models import Request, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item']


class RequestSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Request
        fields = ['items', 'owner', 'address', 'zip_code', 'city', 'tip', 'date']

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
