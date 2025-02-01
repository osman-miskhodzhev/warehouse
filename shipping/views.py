from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.base import TemplateView

from .models import (
    Сounterparty,
    ShippingInvoice,
    Shipment
)
from .forms import (
    СounterpartyForm,
    ShippingInvoiceForm,
    ShipmentForm
)


class MainView(TemplateView):
    """Главное представление отображающее основные таблицы"""

    template_name = 'shipping/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contractors"] = Сounterparty.objects.all()
        context["shippingInvoices"] = ShippingInvoice.objects.all()
        context["shipments"] = Shipment.objects.all()
        return context


class СounterpartyAdd(CreateView):
    """Добавление Контрагента"""

    form_class = СounterpartyForm
    template_name = 'form.html'
    succes_url = 'shipping:mainview'

    def form_valid(self, form):
        Сounterparty.objects.create(**form.cleaned_data)
        return redirect(self.succes_url)


class СounterpartyUpdate(UpdateView):
    """Обновление информации о Контрагенте"""

    model = Сounterparty
    template_name = 'form.html'
    success_url = reverse_lazy('shipping:mainview')
    fields = ('name',)


class СounterpartyDelete(DeleteView):
    """Удаление Контрагента"""

    model = Сounterparty
    success_url = reverse_lazy('shipping:mainview')
    template_name = 'delete.html'


class ShippingInvoiceAdd(CreateView):
    """Добавление Накладной на выгрузку"""

    form_class = ShippingInvoiceForm
    template_name = 'form.html'
    succes_url = 'shipping:mainview'

    def form_valid(self, form):
        ShippingInvoice.objects.create(**form.cleaned_data)
        return redirect(self.succes_url)


class ShippingInvoiceUpdate(UpdateView):
    """Обновление Накладной на выгрузку"""

    model = ShippingInvoice
    template_name = 'form.html'
    success_url = reverse_lazy('shipping:mainview')
    fields = ('conterparty',)


class ShippingInvoiceDelete(DeleteView):
    """Удаление Накладной на выгрузку"""

    model = ShippingInvoice
    success_url = reverse_lazy('shipping:mainview')
    template_name = 'delete.html'


class ShipmentAdd(CreateView):
    """Добавить Выгрузку"""

    form_class = ShipmentForm
    template_name = 'form.html'
    succes_url = 'shipping:mainview'

    def form_valid(self, form):
        Shipment.objects.create(**form.cleaned_data)
        return redirect(self.succes_url)


class ShipmentUpdate(UpdateView):
    """Обновить Выгрузку"""

    model = Shipment
    template_name = 'form.html'
    success_url = reverse_lazy('shipping:mainview')
    fields = ('shippingInvoice', 'product')


class ShipmentDelete(DeleteView):
    """Удалить выгрузку"""

    model = Shipment
    success_url = reverse_lazy('shipping:mainview')
    template_name = 'delete.html'
