from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, CreateView
from .forms import CarForm, CustomerForm, SaleForm, SearchForm
from django.views.generic import CreateView
from .forms import *

class CarCreateView(CreateView):
    form_class = CarForm
    template_name = 'car_form.html'

class CustomerCreateView(CreateView):
    form_class = CustomerForm
    template_name = 'customer_form.html'

class SaleCreateView(CreateView):
    form_class = SaleForm
    template_name = 'sale_form.html'

class SearchView(FormView):
    form_class = SearchForm
    template_name = 'search_form.html'

