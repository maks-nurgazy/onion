from django.db import models

from user.models import Users


class Subscription(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.BooleanField()
