from django.conf.urls import url, include
from django.http import HttpRequest

from paypal import views


urlpatterns = [

    # url(r'^payment-url/$', views.view_that_asks_for_money),
    url(r'^$', views.view_that_asks_for_money),
    url(r'^paypal/ipn$', views.view_that_asks_for_money),
    url(r'^paypal/pro$', views.buy_my_item),
    url(r'^paypal/success$', views.success),
    url(r'^paypal/ipnlistener', include('paypal.standard.ipn.urls')),
]