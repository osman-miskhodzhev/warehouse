from django.db import models


class Provider(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название',
    )


class UploadInvoice(models.Model):
    provider = models.ForeignKey(
        "Provider",
        verbose_name=('Приходная накладная'),
        on_delete=models.CASCADE,
    )


class Upload(models.Model):
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
