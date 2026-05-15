from django.urls import path
from django.shortcuts import render
from .models import SeedEntry
from .views import home, import_success  # we'll define these in views.py

urlpatterns = [
    path('', home, name='home'),                     # root → import page
    path('import-success/', import_success, name='import_success'),
]
