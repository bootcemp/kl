from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from my_shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


class Cart:
    def remove(self, product):
        pass

@require_POST
def cart_add(request, product_id):
    cart_instance = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart_instance.add(product=product, quantity=cd['quantity'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart_instance = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart_instance.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart_instance = Cart(request)
    for item in cart_instance:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart_instance})


def cart():
    return None