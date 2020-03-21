from django.db import models
from django.utils import timezone

# Create your models here.

class ShoppingRequest(models.Model):
    address_street = models.CharField(max_length=100, blank=False)
    address_city = models.CharField(max_length=100, blank=False)
    address_zip_code = models.CharField(max_length=100, blank=False)
    address_c_o = models.CharField(max_lenght=100, blank=True)
    tip = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now())
    accepted_user = models.ForeignKey(ShoppingUser, on_delete=models.SET_NULL)
    delivery_confirmed = models.BooleanField()
    payment_sent = models.BooleanField()
    payment_received = models.BooleanField()

class ShoppingList(models.Model):
    shopping_request = models.ForeignKey(ShoppingRequest, on_delete=models.CASCADE)
    max_price = models.IntegerField()

class ShoppingItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    item = models.CharField()

class Rating(models.Model):
    source_user = models.ForeignKey(ShoppingUser)
    target_user = models.ForeignKey(ShoppingUser)
    rating = models.FloatField
    comment = models.CharField(max_lenght=500, blank=True, default='')

class ShoppingUser(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    location_lat = 
    location_long =
    location_range = IntegerField()
    phone_number = 
    verified = models.BooleanField()
    payment = models.CharField(max_lenght=50, default='PayPal')
    profile_pic = models.ImageField(upload_to='/uploads/')


