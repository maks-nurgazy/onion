from django.db import models

from client.models import Client
from debt_sale.models import DebtSale
from user.models import User


class DeptPayment(models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    sum = models.FloatField()
    date = models.DateField()
    id_debtSales = models.ForeignKey(DebtSale, on_delete=models.CASCADE)
