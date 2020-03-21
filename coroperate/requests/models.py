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
    pass


class ShoppingItem(models.Model):
    """
    An item in a shopping list.
    """
    pass
