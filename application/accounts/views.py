from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def index(request):
    form = UserForm()
    return render(request, "index.html", {"form": form})