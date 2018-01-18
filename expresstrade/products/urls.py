from django.conf.urls import url

from .views import (
    ProductListView,
    ProductDetailSlugView,
)

urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),

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
