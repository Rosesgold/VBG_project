from django.db import models


class User(models.Model):
    login = models.CharField(max_length=10, blank=False)
    password = models.CharField(max_length=16, blank=False)


class Card(models.Model):
    title = models.CharField(max_length=15, blank=False)
    country = models.CharField(max_length=15, blank=False)
    type = models.CharField(max_length=10, blank=False)
    date_of_creating = models.CharField(max_length=10, blank=False)
