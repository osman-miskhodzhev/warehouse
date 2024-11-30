from django.db import models

class Unit(models.Model):
    name = models.CharField(max_length=120)

class Product(models.Model):
    name = models.CharField(max_length=120)
    quantity = models.PositiveIntegerField()
    unit = models.ForeignKey(
        "Unit",
        on_delete=models.CASCADE,
    )
