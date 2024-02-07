from django.contrib import admin
from .models import *


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'shop']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'shop', 'created_date', 'is_paid']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


@admin.register(DailyData)
class DailyDataAdmin(admin.ModelAdmin):
    list_display = ['shop', 'total_amount', 'total_quantity']
