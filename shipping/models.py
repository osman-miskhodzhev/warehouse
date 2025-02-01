from django.db import models

from products.models import Product


class Сounterparty(models.Model):
    """Модель таблицы Контрагент"""

    name = models.CharField(
        max_length=120,
        verbose_name='Название контрагента'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'


class ShippingInvoice(models.Model):
    """Модель таблицы Накладной на выгрузку"""

    conterparty = models.ForeignKey(
        "Сounterparty",
        on_delete=models.CASCADE,
        verbose_name='Контрагент'
    )

    def __str__(self):
        return f'Накладная № {self.id}'

    class Meta:
        verbose_name = 'Накладная на выгрузку'
        verbose_name_plural = 'Накладные на выгрузку'


class Shipment(models.Model):
    """Модель таблицы Выгрузка"""

    shippingInvoice = models.ForeignKey(
        "ShippingInvoice",
        on_delete=models.CASCADE,
        verbose_name='Накладная'
    )
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Товар'
    )

    def __str__(self):
        return f'Выгрузка {self.product.name} \
            по накладной № {self.shippingInvoice.id}'

    class Meta:
        verbose_name = 'Выгрузка'
        verbose_name_plural = 'Выгрузки'
