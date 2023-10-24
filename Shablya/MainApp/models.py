from django.db import models


class User(models.Model):
    login = models.CharField(max_length=10, blank=False)
    password = models.CharField(max_length=16, blank=False)

