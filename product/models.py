from django.db import models
from core.models import BaseModel
from django.utils.text import slugify
from django.urls import reverse


class Discount(BaseModel):
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


class Category(BaseModel):
    name = models.CharField(max_length=20)
    category_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='scategory')
    is_sub = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product:category_filter ', args=[self.slug, ])


class Product(BaseModel):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    category = models.ManyToManyField(Category, related_name='products')
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    discount_id = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    brand = models.CharField(max_length=40)
    inventory = models.CharField(max_length=30)
    image = models.ImageField(upload_to='static/img')
    description = models.TextField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.slug, ])
