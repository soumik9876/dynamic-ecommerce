from django.db import models

from accounts.models import User
from core.models import BaseModel, Address
from django.utils.translation import gettext_lazy as _


class Shop(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_('Shop Name'))
    owner = models.ForeignKey(User, verbose_name=_('Owner'), on_delete=models.CASCADE)
    address = models.OneToOneField(Address, verbose_name=_('Address'), on_delete=models.SET_NULL, null=True)
    is_open = models.BooleanField(verbose_name=_('Is Open'), default=True)
    avatar_image = models.ImageField(verbose_name=_('Avatar Image'), null=True, blank=True)

    class Meta:
        verbose_name = _('Shop')
        verbose_name_plural = _('Shops')

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('Category Name'))
    description = models.TextField(verbose_name=_('Description'), blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('Product Name'))
    description = models.TextField(verbose_name=_('Description'), blank=True)
    category = models.ForeignKey(Category, verbose_name=_('Category'), on_delete=models.SET_NULL, null=True, blank=True)
    shop = models.ForeignKey(Shop, verbose_name=_('Shop'), on_delete=models.CASCADE)
    price = models.FloatField(verbose_name=_('Price'), default=0)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class Cart(BaseModel):
    user = models.OneToOneField(User, verbose_name=_('Cart'), on_delete=models.CASCADE)
    item_total = models.FloatField(verbose_name=_('Subtotal'), default=0)
    total_quantity = models.PositiveIntegerField(verbose_name=_('Total quantity'), default=0)

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    def __str__(self):
        return self.user.username

    def empty_cart(self):
        self.cartitem_set.all().delete()

    # def get_item_total(self):


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, verbose_name=_('Cart'), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_('Product'), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'), default=1)

    class Meta:
        verbose_name = _('Cart Item')
        verbose_name_plural = _('Cart Items')

    @property
    def item_total(self):
        return self.quantity * self.product.price


class Order(BaseModel):
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.SET_NULL, null=True)
    shop = models.ForeignKey(Shop, verbose_name=_('Shop'), on_delete=models.SET_NULL, null=True)
    item_total = models.FloatField(verbose_name=_('Item Total'), default=0)
    delivery_fee = models.FloatField(verbose_name=_('Delivery Fee'), default=0)
    total_amount = models.FloatField(verbose_name=_('Total amount'), default=0)
    is_paid = models.BooleanField(verbose_name=_('Is paid'), default=False)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f'{self.user.username}::{self.shop.name}'


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, verbose_name=_('Cart'), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_('Product'), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'), default=1)

    class Meta:
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')

    @property
    def item_total(self):
        return self.quantity * self.product.price
