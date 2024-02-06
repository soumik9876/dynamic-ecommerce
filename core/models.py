from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    """
        Base model for inheriting common fields
    """
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Constant(BaseModel):
    key = models.CharField(max_length=255, verbose_name=_('Key'), unique=True)
    value = models.TextField(verbose_name=_('Value'))

    def __str__(self):
        return self.key


class BaseAddress(BaseModel):
    country = models.CharField(max_length=40, verbose_name=_('Country'))
    state = models.CharField(max_length=40, verbose_name=_('State'), blank=True)
    city = models.CharField(max_length=40, verbose_name=_('City'))
    street_number = models.CharField(max_length=40, verbose_name=_('Street Number'), blank=True)
    street_name = models.CharField(max_length=40, verbose_name=_('Street Name'), blank=True)
    zip = models.CharField(max_length=20, verbose_name=_('ZIP'), blank=True)

    class Meta:
        abstract = True


class Address(BaseAddress):
    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
