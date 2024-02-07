from django.urls import path

from shop.api.v1.views import *

urlpatterns = [
    path('shop/', ShopListCreateAPIView.as_view(), name='shop-list-create'),
    path('shop/item/', ShopRetrieveUpdateDestroyAPIView.as_view(), name='shop-rud'),
    path('product/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('product/item/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-rud'),
    path('order/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('order/shop/', SellerOrderListAPIView.as_view(), name='seller-order-list'),
    path('cart/item/', CartRetrieveUpdateAPIView.as_view(), name='cart-item')
]
