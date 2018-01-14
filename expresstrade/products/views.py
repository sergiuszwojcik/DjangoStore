from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product


# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "product/product_list_view.html", context)
