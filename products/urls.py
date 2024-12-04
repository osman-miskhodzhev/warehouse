from django.urls import path
from .views import (
    MainView,
    ProductAdd,
    ProductUpdate,
    ProductDelete,
    UnitAdd,
    UnitUpdate,
    UnitDelete
)

app_name = 'products'

urlpatterns = [
    path('', MainView.as_view(), name='main'),

    path('add/', ProductAdd.as_view(), name='add_product'),
    path(
        'update-product/<int:pk>/',
        ProductUpdate.as_view(),
        name='update_product'
    ),
    path(
        'delete-product/<int:pk>/',
        ProductDelete.as_view(),
        name='delete_product'
    ),

    path('add-unit/', UnitAdd.as_view(), name='add_unit'),
    path('update-unit/<int:pk>/', UnitUpdate.as_view(), name='update_unit'),
    path('delete-unit/<int:pk>/', UnitDelete.as_view(), name='delete_unit'),
]
