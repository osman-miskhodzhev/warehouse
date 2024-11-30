from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product
from .forms import ProductForm


def main(request):
    template = 'main.html'
    context = {
        'products': Product.objects.all()
    }
    return render(request, template, context)


class ProductAdd(CreateView):
    form_class = ProductForm
    template_name = 'add.html'
    succes_url = 'products:main'

    def form_valid(self, form):
        Product.objects.create(**form.cleaned_data)
        return redirect(self.succes_url)


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'add.html'
    success_url = reverse_lazy('products:main')
    fields = ('name', 'quantity')


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products:main')
    template_name = 'delete.html'

