"""expresstrade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from .views import home_page, contact_page, login_page, register_page, logout_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^contact/', contact_page, name='contact'),
    url(r'^login/$', login_page, name='login'),
    url(r'^register/$', register_page, name='register'),
    url(r'^products/', include("products.urls", namespace="products")),
    url(r'^search/', include("searchbox.urls", namespace="search")),
    url(r'^cart/', include("cart.urls", namespace="cart"))

]
# Media files are all whatever we upload ourselves
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# OLD VERSION

# from products.views import (
#     ProductListView,
#     ProductDetailView,
#     ProductDetailSlugView,
#     ProductFeaturedDetailView,
#     ProductFeaturedListView)

# URLS

# url(r'^products/$', ProductListView.as_view()),
# url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
# url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
# url(r'^featured/$', ProductFeaturedListView.as_view()),
# url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
