from django.db import models
from clients.models import Client
from products.models import Product

class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    client = models.ForeignKey(Client, blank=False, null=True, verbose_name='Client', on_delete=models.CASCADE)
    date_create = models.DateTimeField(blank=False, null=False, auto_now_add=True, verbose_name='Date')
    payment_method = models.CharField(blank=False, null=False, max_length=20, default='', editable=True, verbose_name='Payment method')
    delivery_method = models.CharField(blank=False, null=False, max_length=50, default='', editable=True, verbose_name='Delivery method')
    delivery_date = models.DateTimeField(blank=False, null=False, default='', editable=True, verbose_name='Delivery date')
    total_price = models.FloatField(blank=False, null=False, max_length=20, default='', editable=True, verbose_name='Sub total')

class Cart(models.Model):
    class Meta:
        db_table = 'carts'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    order = models.ForeignKey(Order, blank=False, null=True, verbose_name='Order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=False, null=True, verbose_name='Order', on_delete=models.CASCADE)
    date_create = models.DateTimeField(blank=False, null=False, default='01/01/0001', verbose_name='Date')
    product_quantity = models.IntegerField(blank=False, null=False, default='', editable=True, verbose_name='Product Qty')
    item_price = models.FloatField(blank=False, null=False, default='', editable=True, verbose_name='Item price')
    sub_total = models.FloatField(blank=False, null=False, default='', editable=True, verbose_name='Sub total')
