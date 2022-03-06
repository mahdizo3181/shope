from django.db import models
from core.models import BaseModel
from product.models import Product
from customer.models import User


class Order(BaseModel):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.customer_id} - {self.id}'

    """
    method get_total_price : khode sefaresh ro darim (ORDER) aval miad hamey items haro migire  bad tosh halghe for mizane tamam item haro migire bad jam mikone.
    """

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(BaseModel):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.id

    def get_cost(self):
        return self.product.price * self.quantity


class OffCode(BaseModel):
    code = models.CharField(max_length=30, null=False, unique=True)
    value = models.PositiveIntegerField(null=False)
    type = models.CharField(max_length=10, choices=[('price', 'Price'), ('percent', 'Percent')], null=False)
    max_price = models.PositiveIntegerField(null=True, blank=True)

    def profit_value(self, price: int):
        """
        Calculate and Return the profit of the discount
        :param price: int (item value)
        :return: profit
        """
        if self.type == 'price':
            return min(self.value, price)
        else:  # percent
            raw_profit = int((self.value / 100) * price)
            return int(min(raw_profit, int(self.max_price))) if self.max_price else raw_profit
