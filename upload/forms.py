from django import forms

from .models import Provider, UploadInvoice, Upload


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        exclude = ()


class UploadInvoiceForm(forms.ModelForm):
    class Meta:
        model = UploadInvoice
        exclude = ()


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        exclude = ()
