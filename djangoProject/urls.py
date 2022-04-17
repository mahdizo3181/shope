"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from order.apis import OrderItemApi, OrderItemDetailApi
from order.views import OrderItemDetailView, OrderView, CustomerOrder
from product.views import *
from customer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('product/', include('product.urls'), name='product'),
    path('accounts/', include('customer.urls', namespace='accounts')),
    path('order/<int:pk>', OrderItemApi.as_view()),
    path('cart/', OrderItemDetailView.as_view(), name='cart'),
    path('orderitem/<int:pk>', OrderItemDetailApi.as_view(), name='order_item'),
    path('rosetta/', include('rosetta.urls')),
    path('update_item/', updateItem, name='update_item'),
    path('address/', UserAddress.as_view(), name='address'),
    path('order/', OrderView.as_view(), name='order'),
    path('orders/', CustomerOrder.as_view(), name='orders')

]
