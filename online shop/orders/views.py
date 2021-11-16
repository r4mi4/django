from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.http import require_POST
from cart.cart import Cart
from .forms import CouponForm
from .models import Order, OrderItem, Coupon
from suds.client import Client


@login_required
def detail(request, order_id):
    form = CouponForm()
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order.html', {'order': order, 'form': form})


@login_required
def order_create(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user)
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
    cart.clear()
    return redirect('orders:detail', order.id)


MERCHANT = 'b0bbe58e-cbf8-11ea-a34f-000c295eb8fc'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
CallbackURL = 'http://localhost:8000/orders/verify/'  # Important: need to edit for really server.


@login_required
def payment(request, order_id, price):
    global amount, o_id
    o_id = order_id
    amount = price
    result = client.service.PaymentRequest(MERCHANT, amount, description, request.user.email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))


@login_required
def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            order = Order.objects.get(id=o_id)
            order.paid = True
            order.save()
            messages.success(request, 'Transaction was successful.', 'success')
            return redirect('shop:home')
        elif result.Status == 101:
            return HttpResponse('Transaction submitted ')
        else:
            return HttpResponse('Transaction failed.')
    else:
        return HttpResponse('Transaction failed or canceled by user')


@require_POST
def coupon_apply(request, order_id):
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__exact=code, valid_from__lte=now, valid_to__gte=now, active=True)
        except Coupon.DoesNotExist:
            messages.error(request, 'This coupon does not exist .', 'danger')
            return redirect('orders:detail', order_id)
        order = Order.objects.get(id=order_id)
        order.discount = coupon.discount
        order.save()
    return redirect('orders:detail', order_id)
