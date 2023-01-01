from django.urls import path
from . import views

urlpatterns = [
    path("", views.products),
    path("sell/", views.sell),
    path("created/", views.created),
]