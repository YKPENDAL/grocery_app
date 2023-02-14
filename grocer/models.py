from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    img = models.ImageField(upload_to='pic')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.CharField(max_length=10)
    type = models.CharField(max_length=10, default="v")
    status = models.BooleanField(True)

    def __str__(self):
        return self.name


class Post(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.IntegerField()
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    phone = models.CharField(max_length=111, default="")
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    pincode = models.CharField(max_length=111)
    
   

