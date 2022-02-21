from django.test import TestCase
from order.models import OffCode, Order, OrderItem
from customer.models import *
from product.models import *


class OffCodeTest(TestCase):
    def setUp(self) -> None:
        self.discount1 = OffCode.objects.create(code='123', value=20, type='percent')
        self.discount2 = OffCode.objects.create(code='12344', value=5000, type='price')
        self.discount3 = OffCode.objects.create(code='1234', value=30, type='percent', max_price='10000')

    def test1_profit_price10000(self):
        self.assertEqual(self.discount1.profit_value(10000), 2000)
        self.assertEqual(self.discount2.profit_value(10000), 5000)
        self.assertEqual(self.discount3.profit_value(10000), 3000)

    def test2_profit_price100000(self):
        self.assertEqual(self.discount1.profit_value(100000), 20000)
        self.assertEqual(self.discount2.profit_value(100000), 5000)
        self.assertEqual(self.discount3.profit_value(100000), 10000)

    def test3_profit_price7000(self):
        self.assertEqual(self.discount1.profit_value(7000), 1400)
        self.assertEqual(self.discount2.profit_value(7000), 5000)
        self.assertEqual(self.discount3.profit_value(7000), 2100)

    def test4_profit_price7111(self):
        self.assertEqual(self.discount1.profit_value(7111), 1422)
        self.assertEqual(self.discount2.profit_value(7111), 5000)
        self.assertEqual(self.discount3.profit_value(7111), 2133)

    def test5_profit_price2000(self):
        self.assertEqual(self.discount1.profit_value(2000), 400)
        self.assertEqual(self.discount2.profit_value(2000), 2000)
        self.assertEqual(self.discount3.profit_value(2000), 600)


class TestOrderItem(TestCase):
    def setUp(self) -> None:
        self.province = Province.objects.create(name='hamedan')
        self.city = City.objects.create(name='hamedan', province_id=self.province)
        self.user = User.objects.create(email='mahdi', phone='09305251819', fullname='mahdizo')
        self.order = Order.objects.create(customer_id=self.user, amount=4)
        self.category = Category.objects.create(name='mobile')
        self.product = Product.objects.create(name='samsung', price=100, brand='samsung',
                                              inventory=4, description='salammmmm')
        self.order_item = OrderItem.objects.create(ordget_coster=self.order, product=self.product, quantity=3)
        self.order_item = OrderItem.objects.create(ordget_coster=self.order, product=self.product, quantity=3)

    def test_get_coster(self):
        self.assertEqual(self.order_item.get_cost(), 250)

    def test_get_total_price(self):
        self.assertEqual(self.order.get_total_price(), 40)
