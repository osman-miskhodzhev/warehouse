from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from .models import Product, Unit
from .forms import ProductForm, UnitForm


class MainView(TemplateView):
    template_name = "products/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        context["units"] = Unit.objects.all()
        return context


class ProductAdd(CreateView):
    form_class = ProductForm
    template_name = 'form.html'
    succes_url = 'products:main'

    def form_valid(self, form):
        Product.objects.create(**form.cleaned_data)
        return redirect(self.succes_url)


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'form.html'
    success_url = reverse_lazy('products:main')
    fields = ('name', 'quantity')


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products:main')
    template_name = 'delete.html'


# Для таблицы Unit

class UnitAdd(CreateView):
    form_class = UnitForm
    template_name = 'form.html'
    succes_url = 'products:main'

    def form_valid(self, form):
        Unit.objects.create(**form.cleaned_data)
        return redirect(self.succes_url)


class UnitUpdate(UpdateView):
    model = Unit
    template_name = 'form.html'
    success_url = reverse_lazy('products:main')
    fields = ('name',)


class UnitDelete(DeleteView):
    model = Unit
    success_url = reverse_lazy('products:main')
    template_name = 'delete.html'
