from django.db import models


class User(models.Model):
    userName = models.CharField(max_length=20)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=30)
    registrationDate = models.DateField()
