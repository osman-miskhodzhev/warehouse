from django import forms

from .models import Product, Unit


class ProductForm(forms.ModelForm):
    class Meta(object):
        model = Product
        exclude = ()


class UnitForm(forms.ModelForm):
    class Meta(object):
        model = Unit
        exclude = ()
