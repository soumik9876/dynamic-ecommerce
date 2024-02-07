from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAddress


# Create your models here.

class User(AbstractUser):
    class UserTypes(models.TextChoices):
        SELLER = 'seller', _('SELLER')
        BUYER = 'buyer', _('BUYER')

    user_type = models.CharField(
        max_length=10, verbose_name=_('User type'), choices=UserTypes.choices,
        default=UserTypes.BUYER
    )

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

    def empty_user_cart(self):
        from shop.models import Cart
        cart = Cart.objects.get(user=self)
        cart.empty_cart()


class UserAddress(BaseAddress):
    is_default = models.BooleanField(verbose_name=_('Is default'), default=False)
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name=_('Phone'), blank=True)

    class Meta:
        verbose_name = _('User Address')
        verbose_name_plural = _('User Addresses')

    def __str__(self):
        return f'{self.user.email} :: {self.id}'
