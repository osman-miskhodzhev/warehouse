from django.urls import path
from .views import MainView, ProductAdd, ProductUpdate, ProductDelete, UnitAdd, UnitUpdate, UnitDelete

app_name = 'products'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('add/', ProductAdd.as_view(), name='add_product'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='delete_product'),
    path('add_unit/', UnitAdd.as_view(), name='add_unit'),
    path('update_unit/<int:pk>/', UnitUpdate.as_view(), name='update_unit'),
    path('delete_unit/<int:pk>/', UnitDelete.as_view(), name='delete_unit'),
]