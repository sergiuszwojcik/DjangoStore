from django.conf.urls import url

from .views import (
    cart_home
)

urlpatterns = [
    # name='detail' can be used as a shortcut to get here
    url(r'^$', cart_home, name='cart'),

]
