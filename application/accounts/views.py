from .forms import SignUpForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from products.models import Product

# Create your views here.
def index(request):
    return render(request, "accounts/index.html")

def profiles(request):
    users = User.objects.all()
    products = Product.objects.all()
    try:
        name = request.GET["current"]
    except:
        name = None
    return render(request, "accounts/profiles.html", {"users":users, "name":name, "products": products})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})