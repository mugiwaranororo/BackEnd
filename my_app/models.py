from django.db import models
from django.contrib.auth.models import User

#the brand, color and type models are used to create the sunglasses
class Brand(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

#here the price and the user are automatically inserted
class Sunglasses(models.Model):
    name = models.CharField(max_length=15)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, default=1)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='static/', default='static/my_app/sunglasses.jpg')

    def __str__(self):
        return self.name
