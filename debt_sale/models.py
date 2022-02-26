from django.db import models

from client.models import Client
from product.models import Product
from user.models import User


class DebtSale (models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    created_date = models.DateField()
    updated_date = models.DateField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    end_date = models.DateField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    debt = models.FloatField()
    status = models.BooleanField()
    paid_date = models.DateField()
