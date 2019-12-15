from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Information(models.Model):
    addressline1 = models.TextField(max_length=100)
    addressline2 = models.TextField(max_length=50)
    addressline3 = models.TextField(max_length=50)
    phone = models.TextField(max_length=50)
    time = models.TextField(max_length=50)

    def __str__(self):
        return self.addressline1