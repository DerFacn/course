from django.db import models
from django.contrib.auth.models import User

# Create your models here.
User._meta.get_field('email')._unique = True
User._meta.get_field('username')._unique = True

class Product(models.Model):
    product_dt = models.DateTimeField(auto_now=True, verbose_name="Час створення")
    product_username = models.CharField(max_length=100, unique=True, verbose_name="Username")
    product_name = models.CharField(max_length=100, verbose_name="Ім'я продавця")
    product_lastname = models.CharField(max_length=100, verbose_name="Фамілія продавця")
    product_phone = models.CharField(max_length=20, unique=True, verbose_name="Номер телефону")
    product_email = models.CharField(max_length=254, unique=True)
    product_productname = models.CharField(max_length=100)
    product_description = models.CharField(max_length=500)
    product_media = models.FileField(upload_to="uploads/")

    def __str__(self):
        return self.product_username

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"