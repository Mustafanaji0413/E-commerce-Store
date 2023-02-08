from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MZEq2EVyRwq0JlP1L8m9sDlf45R3E7Dqsi3KhUGCoM3DjgzykgDluzQVo78ITdOukuqpEGUSBe1hRz9oriFiv9Q00DUdVgPK4',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)