from django import forms
from .models import Car, Customer, Sale

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['marca', 'modelo', 'año']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['nombre', 'apellido', 'email']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['coche', 'cliente', 'fecha']

class SearchForm(forms.Form):
    consulta = forms.CharField()
