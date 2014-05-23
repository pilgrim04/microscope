from views import *
from django.conf.urls import url, patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^list/$', ListView.as_view(), name="list"),
                       url(r'^myorderitem/$', MyOrderItemView.as_view(), name="myorderitem"),
                       url(r'^myorders/$', MyOrdersView.as_view(), name="myorders"),
                       url(r'^orderitem/$', OrderItemView.as_view(), name="orderitem"),
                       url(r'^orders/$', OrdersView.as_view(), name="orders"),
    )


