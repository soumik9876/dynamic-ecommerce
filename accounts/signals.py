from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from shop.models import Cart


@receiver(post_save, sender=User)
def create_cart(sender, instance: User, created, **kwargs):
    """
        Each user will have a cart by default where they will add items
    """
    try:
        cart = Cart.objects.get(user=instance)
    except:
        Cart.objects.create(user=instance)
