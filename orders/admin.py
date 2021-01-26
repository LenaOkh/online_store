from django.contrib import admin
from .models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'client',
        'date_create',
        'payment_method',
        'delivery_method',
        'delivery_date',
        'total_price'
    ]
