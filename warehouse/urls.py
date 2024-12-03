from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('products.urls')),
    path('shipment/', include('shipping.urls')),
    path('upload/', include('upload.urls')),
    path('admin/', admin.site.urls),
]
