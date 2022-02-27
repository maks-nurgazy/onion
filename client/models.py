from django.db import models


class Client(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    inn = models.BigIntegerField()
    phone = models.CharField(max_length=10)
    extraPhones = models.CharField(max_length=50, blank=True)
    images = models.ImageField(blank=True)
    refImages = models.ImageField(blank=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName
