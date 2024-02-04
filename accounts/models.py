from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


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
