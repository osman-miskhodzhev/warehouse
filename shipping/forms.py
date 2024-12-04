from django import forms

from .models import Сounterparty, ShippingInvoice, Shipment


class СounterpartyForm(forms.ModelForm):
    class Meta(object):
        model = Сounterparty
        exclude = ()


class ShippingInvoiceForm(forms.ModelForm):
    class Meta(object):
        model = ShippingInvoice
        exclude = ()


class ShipmentForm(forms.ModelForm):
    class Meta(object):
        model = Shipment
        exclude = ()
