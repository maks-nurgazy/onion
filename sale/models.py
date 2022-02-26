from django.db import models

from product.models import Product
from user.models import User


class Sale(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    createdDate = models.DateField()
    updatedDate = models.DateField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
