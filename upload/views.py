from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from .models import Provider, UploadInvoice, Upload
from .forms import ProviderForm, UploadInvoiceForm, UploadForm

def main(request):
    template_name = 'upload/main.html'
    context = {
        'providers': Provider.objects.all(),
        'invocies': UploadInvoice.objects.all(),
        'uploads': Upload.objects.all(),
    }
    return render(request, template_name, context)


class ProviderAdd(CreateView):
    form_class = ProviderForm
    template_name = 'form.html'
    succes_url = 'uploading:upload_view'

    def form_valid(self, form):
        Provider.objects.create(**form.cleaned_data)
        return redirect(self.succes_url)


class ProviderUpdate(UpdateView):
    model = Provider
    template_name = 'form.html'
    success_url = reverse_lazy('uploading:upload_view')
    fields = ('name',)


class ProviderDelete(DeleteView):
    model = Provider
    success_url = reverse_lazy('uploading:upload_view')
    template_name = 'delete.html'


class UploadInvoiceAdd(CreateView):
    form_class = UploadInvoiceForm
    template_name = 'form.html'
    succes_url = 'uploading:upload_view'

    def form_valid(self, form):
        UploadInvoice.objects.create(**form.cleaned_data)
        return redirect(self.succes_url)


class UploadInvoiceUpdate(UpdateView):
    model = UploadInvoice
    template_name = 'form.html'
    success_url = reverse_lazy('uploading:upload_view')
    fields = ('provider',)


class UploadInvoiceDelete(DeleteView):
    model = UploadInvoice
    success_url = reverse_lazy('uploading:upload_view')
    template_name = 'delete.html'


class UploadAdd(CreateView):
    form_class = UploadForm
    template_name = 'form.html'
    succes_url = 'uploading:upload_view'

    def form_valid(self, form):
        Upload.objects.create(**form.cleaned_data)
        return redirect(self.succes_url)


class UploadUpdate(UpdateView):
    model = Upload
    template_name = 'form.html'
    success_url = reverse_lazy('uploading:upload_view')
    fields = ('invoice', 'product')


class UploadDelete(DeleteView):
    model = Upload
    success_url = reverse_lazy('uploading:upload_view')
    template_name = 'delete.html'
