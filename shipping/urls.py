from django.urls import path

from .views import (
    MainView,
    СounterpartyAdd,
    СounterpartyUpdate,
    СounterpartyDelete,
    ShippingInvoiceAdd,
    ShippingInvoiceUpdate,
    ShippingInvoiceDelete,
    ShipmentAdd,
    ShipmentUpdate,
    ShipmentDelete,
)

app_name = 'shipping'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path(
        'add-counterparty/',
        СounterpartyAdd.as_view(),
        name='add_counterparty'
    ),
    path(
        'udate-counterparty/<int:pk>/',
        СounterpartyUpdate.as_view(),
        name='update_counterparty'
    ),
    path(
        'delete_counterparty/<int:pk>/',
        СounterpartyDelete.as_view(),
        name='delete_counterparty'
    ),
    path('add-invoice/', ShippingInvoiceAdd.as_view(), name='add_invoice'),
    path(
        'udate-invoice/<int:pk>/',
        ShippingInvoiceUpdate.as_view(),
        name='update_invoice'
    ),
    path(
        'delete_invoice/<int:pk>/',
        ShippingInvoiceDelete.as_view(),
        name='delete_invoice'
    ),
    path('add-shipment/', ShipmentAdd.as_view(), name='add_shipment'),
    path(
        'udate-shipment/<int:pk>/',
        ShipmentUpdate.as_view(),
        name='update_shipment'
    ),
    path(
        'delete_shipment/<int:pk>/',
        ShipmentDelete.as_view(),
        name='delete_shipment'
    ),
]
