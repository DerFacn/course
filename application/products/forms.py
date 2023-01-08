from django import forms
from .models import Product

class SellForm(forms.Form):
    product_phone = forms.CharField(label="Номер телефону", max_length=20, required=True, error_messages={"required": "Cant be empty!"})
    product_productname = forms.CharField(label="Назва товару", max_length=100, required=True, error_messages={"required": "Cant be empty!"})
    product_description = forms.CharField(label="Опис товару", max_length=500, required=False, error_messages={"max_length": "Max length!"})
    product_media = forms.FileField(label="Зображення товару", max_length=500, required=True, error_messages={"required": "Cant be empty!"})