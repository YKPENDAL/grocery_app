from django.db import models

# Create your models here.
class register (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.IntegerField()
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.BooleanField(True)

    