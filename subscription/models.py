from django.db import models

from user.models import User


class Subscription(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
