from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,

        'stripe_public_key': 'pk_test_51OyZyRGlomcvb3PUq4dG9M0Y1v7E3y9okwmkp8x7UwirDYVMHq9Shc9FP5QeVRH57FYexuk1X1NumqKtPjxqMH7C005YBEJR6Q',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
