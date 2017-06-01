from django.core.urlresolvers import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from paypal.pro.views import PayPalPro
from django.conf import settings

def view_that_asks_for_money(request):

    # What you want the button to do.
    paypal_dict = {
        "business": "sashpro-facilitator@mail.ru",
        "amount": "11.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id11",
        "notify_url": "http://2a53ec9a.ngrok.io" + reverse('paypal-ipn'),
        "return_url": "http://2a53ec9a.ngrok.io/",
        "cancel_return": "http://2a53ec9a.ngrok.io/",
        "custom": "Upgrade all users!",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "ipn/paypal.html", context)


def nvp_handler(nvp):
    # This is passed a PayPalNVP object when payment succeeds.
    # This should do something useful!
    pass

def buy_my_item(request):
    item = {"paymentrequest_0_amt": "12.00",  # amount to charge for item
            "invnum": "2345wertsddf22412",         # unique tracking variable paypal
            "custom": "rwterdte1232r",       # custom tracking variable for you
            "cancelurl": "%s%s" % (settings.ALLOWED_HOSTS[0], "/cancel"),  # Express checkout cancel url
            "returnurl": "%s%s" % (settings.ALLOWED_HOSTS[0], "/return"),  # Express checkout return url
            "amt": 1.0
            }
    ppp = PayPalPro(
              item=item,                            # what you're selling
              # payment_template="payment.html",      # template name for payment
              # confirm_template="confirm.html", # template name for confirmation
              success_url="/paypal/success/",              # redirect location after success
              nvp_handler=nvp_handler)
    return ppp(request)



def success(request):
    return render(request, "pro/success.html")