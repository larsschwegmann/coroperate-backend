from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A user profile for storing information about the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16, default='default phone')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    radius = models.PositiveSmallIntegerField(default=3)
    verified = models.BooleanField(default=False)


class Request(models.Model):
    """
    A request for a shopping service.
    """
    owner = models.ForeignKey(User, related_name='owned_requests')
    max_price = models.DecimalField(max_digits=6, decimal_places=2, default=20)
    address = models.CharField(max_length=32, default='default street')
    zip_code = models.CharField(max_length=10, default='default zip code')
    city = models.CharField(max_length=32, default='default city')
    tip = models.PositiveSmallIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    acceptor = models.ForeignKey(User, related_name='accepted_requests', null=True, on_delete=models.SET_NULL)


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
    receiver = models.ForeignKey(User, related_name='received_ratings', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=CHOICES)
    comment = models.TextField(max_length=128, blank=True, default='')

    class Meta:
        unique_together = ['author', 'receiver']


class Item(models.Model):
    """
    An item requested in a request.
    """
    request = models.ForeignKey(Request, related_name='items', on_delete=models.CASCADE)
    item = models.CharField(max_length=64)
