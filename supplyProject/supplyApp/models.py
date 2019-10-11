from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    supplyCategory = models.CharField(max_length=6)



class PaintSupplyModel(models.Model):
    Date = models.DateTimeField(default=timezone.now)
    SupplyType = models.ForeignKey(Category, on_delete=CASCADE)
    Color = models.CharField(max_length=50)
    Quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=CASCADE)


class BrushSupplyModel(models.Model):
    Date = models.DateTimeField(default=timezone.now)
    SupplyType = models.ForeignKey(Category, on_delete=CASCADE)
    BrushSize = models.CharField(max_length=4)
    BrushType = models.CharField(max_length=10)
    Quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=CASCADE)


class CanvasSupplyModel(models.Model):
    Date = models.DateTimeField(default=timezone.now)
    SupplyType = models.ForeignKey(Category, on_delete=CASCADE)
    Size = models.CharField(max_length=10)
    Quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=CASCADE)