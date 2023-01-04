from django.db import models

# Create your models here.
class Product(models.Model):
    product_dt = models.DateTimeField(auto_now=True, verbose_name="Час створення")
    product_username = models.CharField(max_length=100, verbose_name="Ім'я користувача")
    product_name = models.CharField(max_length=100, verbose_name="Ім'я продавця")
    product_lastname = models.CharField(max_length=100, verbose_name="Прізвище продавця")
    product_phone = models.CharField(max_length=20, verbose_name="Номер телефону")
    product_email = models.CharField(max_length=254, verbose_name="Електронна пошта продавця")
    product_productname = models.CharField(max_length=100, verbose_name="Назва товару")
    product_description = models.CharField(max_length=500, verbose_name="Опис товару")
    product_media = models.ImageField(upload_to="images/", verbose_name="Фотографії товару")

    def __str__(self):
        return self.product_productname

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"