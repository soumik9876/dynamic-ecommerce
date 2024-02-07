from rest_framework.permissions import BasePermission

from accounts.models import User
from shop.models import Shop, Product


class IsSeller(BasePermission):
    """
        Check if the request user is a seller or owner of the shop they want to modify
    """

    def has_permission(self, request, view):
        return request.user.user_type == User.UserTypes.SELLER

    def has_object_permission(self, request, view, obj: Shop):
        return request.method == 'GET' or (
                request.user.is_authenticated and
                obj.owner == request.user
        )


class ProductOwner(BasePermission):
    """
        Checks if user is owner of the shop they want to create or modify product for
    """

    def has_permission(self, request, view):
        if request.method != 'GET':
            shop = int(request.data.get('shop', None))
            print(shop not in list(request.user.shop_set.all().values_list('id', flat=True)))
            if not request.user.is_authenticated or (
                    shop is not None and
                    shop not in list(request.user.shop_set.all().values_list('id', flat=True))
            ):
                return False

        return True

    def has_object_permission(self, request, view, obj: Product):
        return request.method == 'GET' or (
                request.user.is_authenticated and
                obj.shop.owner == request.user
        )
