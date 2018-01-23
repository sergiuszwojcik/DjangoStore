from django.conf.urls import url

from .views import (
    SearchBoxProductListView,
)

urlpatterns = [
    # name='detail' can be used as a shortcut to get here
    url(r'^$', SearchBoxProductListView.as_view(), name='query'),
]
