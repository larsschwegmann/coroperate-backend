from rest_framework import serializers
from requests.models import Request, ShoppingList, ShoppingItem



class ShoppingItemSerializer(serializers.ModelSerializer):
    shopping_list = serializers.ReadOnlyField(source='shopping_list.id')

    class Meta:
        model = ShoppingItem
        fields = ['id', 'item', 'shopping_list']


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ['id', 'request', 'max_price']


class RequestSerializer(serializers.ModelSerializer):
    shopping_list = ShoppingListSerializer(read_only=True)

    class Meta:
        model = Request
        fields = [
            'id', 'owner', 'shopping_list', 'address', 'zip_code','city',
            'tip', 'date', 'accepted'
        ]