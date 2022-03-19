from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import Order
# Create your views here.
def CheckOut(request):
    if request.POST:
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk=uid)
        print(address, phone, pincode, cart, user)
        for i in cart:
            a = cart[i]['price']
            b = cart[i]['quantity']
            total = int(a) * int(b)
            print(i)
            order = Order(
                user = user,
                product = cart[i]['name'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                image = cart[i]['image'],
                address = address,
                phone = phone,
                pincode = pincode,
                total = total
            )

            order.save()
        request.session['cart'] = {}
        return redirect('index')
    return HttpResponse('Это страница оформления')

def YourOrder(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk=uid)
    order = Order.objects.filter(user=user).order_by('-date')

    context={
        'order':order,
    }
    return render(request, 'order.html', context)