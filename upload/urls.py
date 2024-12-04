from django.urls import path

from .views import (
    main,
    ProviderAdd,
    ProviderUpdate,
    ProviderDelete,

    UploadInvoiceAdd,
    UploadInvoiceUpdate,
    UploadInvoiceDelete,

    UploadAdd,
    UploadUpdate,
    UploadDelete,
)

app_name = 'uploading'

urlpatterns = [
    path('upload-view/', main, name='main'),
    path('add-provider/', ProviderAdd.as_view(), name='add_provider'),
    path(
        'update-provider/<int:pk>/',
        ProviderUpdate.as_view(),
        name='update_provider'
    ),
    path(
        'delete-provider/<int:pk>/',
        ProviderDelete.as_view(),
        name='delete_provider'
    ),
    path('add-invoice/', UploadInvoiceAdd.as_view(), name='add_invoice'),
    path(
        'update-invoice/<int:pk>/',
        UploadInvoiceUpdate.as_view(),
        name='update_invoice'
    ),
    path(
        'delete-invoice/<int:pk>/',
        UploadInvoiceDelete.as_view(),
        name='delete_invoice'
    ),
    path('add-upload/', UploadAdd.as_view(), name='add_upload'),
    path(
        'update-upload/<int:pk>/',
        UploadUpdate.as_view(),
        name='update_upload'
    ),
    path(
        'delete-upload/<int:pk>/',
        UploadDelete.as_view(),
        name='delete_upload'
    ),
]
