from django.db import models


class Provider(models.Model):
    """Модель таблицы Поставщик"""

    name = models.CharField(
        max_length=50,
        verbose_name='Название фирмы',
    )

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
    
    def __str__(self):
        return self.name


class UploadInvoice(models.Model):
    """Модель таблицы Накладная"""

    provider = models.ForeignKey(
        "Provider",
        verbose_name=('Поставщик'),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Приходная накладная'
        verbose_name_plural = 'Приходные накладные'
    
    def __str__(self):
        return self.id


class Upload(models.Model):
    """Модель таблицы Выгрузка"""

    invoice = models.ForeignKey(
        "UploadInvoice",
        verbose_name=('Накладная'),
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "products.Product",
        verbose_name=('Товар'),
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Выгрузка'
        verbose_name_plural = 'Выгрузки'
    
    def __str__(self):
        return f'Выгрузка №{self.id} Накладная №{self.invoice.id}'
