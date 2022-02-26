from django.db import models

from user.models import User


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

