from django.db import models
from django.utils.translation import gettext_lazy as _
from client.models import Client
from product.models import Product
from user.models import Users


class DebtSale(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    created_date = models.DateField()
    updated_date = models.DateField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    end_date = models.DateField()
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    debt = models.FloatField()

    class Status(models.TextChoices):
        PAID = 'Paid', _('Оплачено')
        NOT_PAID = 'Not_Paid', _('Не оплачено')

    status = models.CharField(
        max_length=8,
        choices=Status.choices,
        default=Status.NOT_PAID,
    )
    paid_date = models.DateField()

    def __str__(self):
        return self.id_client.firstName + " " + self.id_client.lastName
