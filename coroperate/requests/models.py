from django.db import models


class Profile(models.Model):
    """
    A user profile for storing information about the user.
    """
    pass


class Request(models.Model):
    """
    A request for a shopping service.
    """
    pass


class Rating(models.Model):
    """
    A rating for a user by another user.
    """
    pass


class ShoppingList(models.Model):
    """
    A list of shopping items.
    """
    max_price = models.DecimalField(max_digits=6, decimal_places=2)


class ShoppingItem(models.Model):
    """
    An item in a shopping list.
    """
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=128, blank=True, default='')
