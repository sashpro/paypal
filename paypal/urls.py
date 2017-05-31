from django.conf.urls import url, include

from paypal import views


urlpatterns = [

    url(r'^payment-url/$', views.buy_my_item),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
]