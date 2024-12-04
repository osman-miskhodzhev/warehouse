from django.db import models


class Unit(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name='Название единицы измерения'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Единица измерения'


class Product(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name='Название товара'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество товара'
    )
    unit = models.ForeignKey(
        "Unit",
        on_delete=models.CASCADE,
        verbose_name='Единица имземерния'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товары'
