from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CostumUser(AbstractUser):
    Nombre = models.CharField(max_length=30)
    edad = models.IntegerField(null=True, blank=True)
    pais = models.CharField(max_length=30)