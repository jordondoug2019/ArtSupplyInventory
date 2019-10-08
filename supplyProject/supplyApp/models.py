from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=15)


class Supply(models.Model):
    date_added = models.DateTimeField(default=timezone.now)

