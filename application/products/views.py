from django.shortcuts import render
from .forms import SellForm
from .models import Product

# Create your views here.
def products(request):
    product_list = Product.objects.all()
    return render(request, "products.html", {"product_list": product_list})

def sell(request):
    form = SellForm()
    return render(request, "sell.html", {"form": form})

def created(request):
    product_username = request.user
    name = request.user.first_name
    lastname = request.user.last_name
    email = request.user.email
    phone = request.POST["product_phone"]
    productname = request.POST["product_productname"]
    description = request.POST["product_description"]
    media = request.POST["product_media"]
    product = Product(product_phone = phone, product_productname = productname, product_username = product_username, product_name = name, product_lastname = lastname, product_email = email,
                      product_description = description, product_media = media)
    product.save()
    return render(request, "created.html")
