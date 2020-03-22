from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A user profile for storing information about the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=32, default='address x')
    zip_code = models.CharField(max_length=10, default='zip code x')
    city = models.CharField(max_length=32, default='city x')


class Request(models.Model):
    """
    A request for a shopping service.
    """
    owner = models.ForeignKey(User, related_name='owned_requests', on_delete=models.CASCADE)
    max_price = models.DecimalField(max_digits=6, decimal_places=2, default=20)
    address = models.CharField(max_length=32, default='address x')
    zip_code = models.CharField(max_length=10, default='zip code x')
    city = models.CharField(max_length=32, default='city x')
    tip = models.PositiveSmallIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    acceptor = models.ForeignKey(User, related_name='accepted_requests', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'Request by {self.owner.username} on {self.date}'


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

    def __str__(self):
        f'Rating of {self.rating} from {self.author.username} for {self.receiver.username}'


class Item(models.Model):
    """
    An item requested in a request.
    """
    request = models.ForeignKey(Request, related_name='items', on_delete=models.CASCADE)
    item = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.item}'
