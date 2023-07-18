from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views import generic
from django.views.generic.base import View
from .models import OrderItem, City
from .forms import OrderCreateForm
from cart.cart import Cart
from orders.models import Order
from orders import models, forms
from django.contrib import messages


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'create.html',
                  {'cart': cart, 'form': form})


def updateOrder(request, id):
    order = Order.objects.get(id=id)
    form = OrderCreateForm(instance=order)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'profile.html', context)


def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'City_Dropdown_List.html', {'cities': cities})


def Success(request):
    return render(request, 'contact_success.html')
