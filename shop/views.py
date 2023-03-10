from django.shortcuts import render
from django.views.generic import ListView

from .models import Product

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 10
    template_name = 'shop/list.html'