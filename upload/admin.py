from django.contrib import admin

from .models import Provider, Upload, UploadInvoice

admin.site.register(Provider)
admin.site.register(Upload)
admin.site.register(UploadInvoice)
