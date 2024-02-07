from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveUpdateAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated

from core.api.paginations import StandardResultsSetPagination
from shop.api.v1.permissions import IsSeller, ProductOwner
from shop.api.v1.serializers import ShopSerializer, ProductSerializer, OrderSerializer, CartSerializer
from shop.models import Shop, Product, Order, Cart


class ShopListCreateAPIView(ListCreateAPIView):
    serializer_class = ShopSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated, IsSeller]

    def get_queryset(self):
        return Shop.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ShopRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated, IsSeller]
    filterset_fields = ['id']
    queryset = Shop.objects.all()


class ProductListCreateAPIView(ListCreateAPIView):
    """
        Get method ->  Paginated list of all products
        Post method -> Create product object, request user has to be owner of the shop
    """
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [ProductOwner]
    filterset_fields = ['shop', 'category']

    def get_queryset(self):
        return Product.objects.all()


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [ProductOwner]
    filterset_fields = ['id']
    queryset = Product.objects.all()


class OrderListCreateAPIView(ListCreateAPIView):
    """
        Get -> returns list of orders made by authenticated user
        Post -> Creates an order for user and empties cart
    """
    serializer_class = OrderSerializer
    pagination_class = StandardResultsSetPagination
    filterset_fields = ['shop']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    # def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
    # self.request.user.empty_user_cart()


class SellerOrderListAPIView(ListAPIView):
    """
        List API for Owner shops order list
    """
    permission_classes = [IsAuthenticated, IsSeller]
    serializer_class = OrderSerializer
    filterset_fields = ['shop']

    def get_queryset(self):
        return Order.objects.filter(shop__owner=self.request.user)


class CartRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """
        With update method, items can be updated in cart
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get_object(self):
        return get_object_or_404(Cart, user=self.request.user)
