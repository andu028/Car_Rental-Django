import json, datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import os


def map_view(request):
    maps_key = os.environ.get('Maps_key')
    context = {'maps_key': maps_key}
    return render(request, 'rental_store/map.html', context)


def home(request):
    context = {'title': 'Home'}
    return render(request, 'rental_store/home.html', context)


@login_required
def about(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order['get_cart_items']

    context = {'cartItems': cartItems, 'title': 'About'}
    return render(request, 'rental_store/about.html', context)


@login_required
def rental_store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems, 'title': 'Our Cars'}
    return render(request, 'rental_store/rental_store.html', context)


@login_required
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, 'title': 'Cart'}
        cartItems = order['get_cart_items']

    context = {"items": items, "order": order, 'cartItems': cartItems, 'title': 'Cart'}
    return render(request, 'rental_store/cart.html', context)


@login_required
@csrf_exempt
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order['get_cart_items']

    context = {"items": items, "order": order, 'cartItems': cartItems, 'title': 'Checkout'}
    return render(request, 'rental_store/checkout.html', context)


@login_required
@csrf_exempt
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse({'status': 'ok'})


@login_required
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            phone_number=data['shipping']['phone_number'],
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            county=data['shipping']['county'],
            zipcode=data['shipping']['zipcode'],
        )
    else:
        print('User is not logged in')

    return JsonResponse('Payment submitted..', safe=False)
