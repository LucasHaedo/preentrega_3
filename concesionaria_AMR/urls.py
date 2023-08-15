from django.urls import path
from .views import CarCreateView, CustomerCreateView, SaleCreateView, SearchView

urlpatterns = [
    path('car/create/', CarCreateView.as_view(), name='car_create'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('sale/create/', SaleCreateView.as_view(), name='sale_create'),
    path('search/', SearchView.as_view(), name='search'),
]

