from django.test import TestCase
from product.models import Discount, Product, Category
import pytest


class DiscountTest(TestCase):
    def setUp(self) -> None:
        self.discount1 = Discount.objects.create(value=20, type='percent')
        self.discount2 = Discount.objects.create(value=5000, type='price')
        self.discount3 = Discount.objects.create(value=30, type='percent', max_price='10000')

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


class TestCategory(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name='Mobile Samsung')
        self.category2 = Category.objects.create(name='Camputer')
        self.category3 = Category.objects.create(name='lavazem khanegi')

    def test_save1(self):
        self.assertEqual(self.category1.slug, 'mobile-samsung')

    def test_save2(self):
        self.assertEqual(self.category2.slug, 'camputer')

    def test_save3(self):
        self.assertEqual(self.category3.slug, 'lavazem-khanegi')


class ProductTest(TestCase):
    def setUp(self) -> None:
        self.product1 = Product.objects.create(name='Samsung', price=100, brand='samsung',
                                               inventory=4, description='salammmmm')
        self.product2 = Product.objects.create(name='Nokia 0021', price=100, brand='samsung',
                                               inventory=4, description='salammmmm')
        self.product3 = Product.objects.create(name='Mamad Pelastiki', price=100, brand='samsung',
                                               inventory=4, description='salammmmm')
        self.product4 = Product.objects.create(name='Yakhchale samsung', price=100, brand='samsung',
                                               inventory=4, description='salammmmm')

    def test_save1(self):
        self.assertEqual(self.product1.slug, 'samsung')
        self.assertEqual(self.product2.slug, 'nokia-0021')
        self.assertEqual(self.product3.slug, 'mamad-pelastiki')
        self.assertEqual(self.product4.slug, 'yakhchale samsung')
