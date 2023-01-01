from django import forms
from .models import Product

class SellForm(forms.Form):
    product_phone = forms.CharField(max_length=20, required=True, label="Номер телефону")
    product_productname = forms.CharField(max_length=100, required=True, label="Назва товару")
    product_description = forms.CharField(max_length=500, label="Опис товару")
    product_media = forms.FileField(label="Зображення товару")

    #class ProductForm(forms.ModelForm):
    #    class Meta:
    #        model = Product
    #        exclude = ['product_username', 'product_name', 'product_lastname', 'product_email']