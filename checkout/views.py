from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your bag')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LmklQLKxuGQeWSHosnIdDDgRsRdSdBACSAf2oDuzvwk3IscugzgZyXBEPf5N9nAhDigBZ9nCkmy0DlSw0u6J5Mv00hzkh88Nk',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
