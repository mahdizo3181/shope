from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import OrderItem, Order
from customer.models import Address
from django.views import View
from django.contrib import messages


# Create your views here.


# class OrderItemDetailView(ListView):
#     template_name = 'order/items.html'
#     model = OrderItem
#     context_object_name = 'items'


class OrderItemDetailView(View):
    template_name = 'order/items.html'

    def get(self, request):
        order_items = OrderItem.objects.filter(is_deleted=False).all()
        return render(request, self.template_name, {'items': order_items})


class OrderView(View):
    template_name = 'order/order.html'

    def get(self, request):
        user = request.user
        address = Address.objects.filter(customer_id=user).all
        return render(request, self.template_name, {'address': address})

    def post(self, request):
        form = request.POST
        address_id = int(form['address'])
        address = Address.objects.filter(id=address_id)
        print(address[0])
        user = request.user
        order = OrderItem.objects.filter(customer_id=user).all()
        for orders in order:
            print(orders.order_id.id)
            Order.objects.filter(id=orders.order_id.id).update(address=address[0].id)
            OrderItem.objects.filter(id=orders.id).update(is_deleted=True)
        messages.success(request, '.سفارش شما با موفقیت ثبت شد', 'success')
        return redirect('home:home')


class CustomerOrder(View):
    template_name = 'accounts/orders.html'

    def get(self, request):
        user = request.user
        orders = Order.objects.filter(customer_id=user)
        order_item = OrderItem.objects.filter(customer_id=user, is_deleted=False)
        print(order_item)
        return render(request, self.template_name, {'orders': orders, 'order_item': order_item})
