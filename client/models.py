from django.db import models


class Client(models.Model):
    firsName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    inn = models.CharField(max_length=14)
    phone = models.CharField(max_length=13)
    extraPhones = models.CharField(max_length=50)
    images = models.ImageField()
    refImages = models.ImageField()
