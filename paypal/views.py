from paypal.pro.views import PayPalPro

def nvp_handler(nvp):
    # This is passed a PayPalNVP object when payment succeeds.
    # This should do something useful!
    pass

def buy_my_item(request):
    item = {"paymentrequest_0_amt": "10.00",  # amount to charge for item
            "inv": "inventory",         # unique tracking variable paypal
            "custom": "tracking",       # custom tracking variable for you
            "cancelurl": "http://...",  # Express checkout cancel url
            "returnurl": "http://..."}  # Express checkout return url

    ppp = PayPalPro(
              item=item,                            # what you're selling
              # payment_template="payment.html",      # template name for payment
              # confirm_template="confirm.html", # template name for confirmation
              success_url="/success/",              # redirect location after success
              nvp_handler=nvp_handler)
    return ppp(request)