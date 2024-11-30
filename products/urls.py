from django.urls import path
from .views import main, ProductAdd, ProductUpdate, ProductDelete

app_name = 'products'

urlpatterns = [
    path('', main, name='main'),
    path('add/', ProductAdd.as_view(), name='add_product'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='delete_product'),
]