from django.utils.translation import gettext_lazy as _
from django.db import models

from user.models import Users


class Product(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    class State(models.TextChoices):
        NEW = 'New', _('Новый')
        USED = 'Used', _('Б/У')

    state = models.CharField(
        max_length=4,
        choices=State.choices,
        default=State.NEW,
    )

    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand + " " + self.model
