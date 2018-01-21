from django.conf.urls import url

from .views import (
    ProductListView,
    ProductDetailSlugView,
)

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    # name='detail' can be used as a shortcut to get here
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),

]

# NOT USED URLS FOR TESTING

# from .views import (
# ProductDetailView,
# ProductFeaturedDetailView,
# ProductFeaturedListView
# )

# url(r'^featured/$', ProductFeaturedListView.as_view()),
# url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
# url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
