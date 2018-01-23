from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product



# Create your views here.

# This will be view for searchBox
class SearchBoxProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchBoxProductListView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    # Display view
    def get_queryset(self, *args, **kwargs):
        request = self.request
        print(request)
        query = request.GET.get('q', None)
        print(query)
        # search_query = request.GET.get('q', None)
        if query is not None:
            return Product.objects.search(query)  # products.models ProductManager function for Product model
        else:
            return Product.objects.featured()

        """
        __icontains -> field contains something
        __iexact -> field is exactly something
        ?q=something -> url get parameter
        """
