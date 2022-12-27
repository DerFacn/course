from django.db import models

# Create your models here.
class Users(models.Model):
    user_dt = models.DateTimeField(auto_now=True)
    user_name = models.CharField(max_length = 15)
    user_login = models.CharField(max_length=20)
    user_password = models.CharField(max_length=50)
    user_secret_key = models.CharField(max_length=10)