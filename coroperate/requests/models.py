from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A user profile for storing information about the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    radius = models.PositiveSmallIntegerField(default=3)
    verified = models.BooleanField(default=False)


class Request(models.Model):
    """
    A request for a shopping service.
    """
    shopping_list = models.OneToOneField(shopping_list, on_delete=models.CASCADE)
    address = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=32)
    county = models.CharField(max_length=32)
    tip = models.PositiveSmallIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    accepted = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class Rating(models.Model):
    """
    A rating for a user by another user.
    """ 
    CHOICES = [
        (1, 'horrible'),
        (2, 'bad'),
        (3, 'okay'),
        (4, 'good'),
        (5, 'fantastic')
    ]
    author = models.ForeignKey(User, related_name='authored_ratings', on_delete=models.CASCADE)
    rated = models.ForeignKey(User, related_name='received_ratings', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=CHOICES)
    comment = models.TextField(max_length=128, blank=True, default='')

    class Meta:
        unique_together = ['author', 'rated']


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
    item = models.CharField(max_length=64)
