from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product


# Create your views here.
class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    template_name = "products/featured-detail.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    # class based view method to get context
    # get context by any thing that view is doing
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Product, slug=slug, active=True)
        return instance


class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance

# same as class above generic django DetailView class
# def product_detail_view(request, pk=None, *args, **kwargs):
#     # instance = Product.objects.get(pk=pk) #id
#     instance = get_object_or_404(Product, pk=pk)
#     # try:
#     #     instance = Product.objects.get(id=pk)
#     # except Product.DoesNotExist:
#     #     print("there is no product")
#     # except:
#     #     print("hmm?")
#     context = {
#         'object': instance
#     }
#     return render(request, "products/product_detail_view.html", context)


# This same as generic ListView django class above
# def product_list_view(request):
#     queryset = Product.objects.all()
#     context = {
#         'qs': queryset
#     }
#     return render(request, "product/product_list_view.html", context)
