from django.db import models

from products.models import Product

class Сounterparty(models.Model):
    name = models.CharField(max_length=120)

class ShippingInvoice(models.Model):
    conterparty = models.ForeignKey(
        "Сounterparty",
        on_delete=models.CASCADE,
    )

class Shipment(models.Model):
    shippingInvoice = models.ForeignKey(
        "ShippingInvoice",
        on_delete=models.CASCADE,
    )
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
    )
