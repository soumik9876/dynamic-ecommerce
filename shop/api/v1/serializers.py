from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from shop.models import Shop, Product, Cart, CartItem, Order, OrderItem, DailyData


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        extra_kwargs = {
            'owner': {'read_only': True}
        }


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        extra_kwargs = {
            'cart': {'required': False}
        }


class CartSerializer(WritableNestedModelSerializer):
    cartitem_set = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        extra_kwargs = {
            'order': {'required': False}
        }


class OrderSerializer(WritableNestedModelSerializer):
    orderitem_set = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'is_paid': {'read_only': True},
            'user': {'read_only': True},
            'subtotal': {'read_only': True},
            'total': {'read_only': True}
        }

    def create(self, validated_data):
        """
            Calculating costs and adding user before creating order
        """
        costs = self.calculate_cost(validated_data)
        user = self.context.get('request').user
        validated_data.update({
            **costs,
            'user': user
        })
        user.empty_user_cart()
        return super().create(validated_data)

    def validate_orderitem_set(self, value):
        if len(value) == 0:
            raise ParseError('Minimum one item required!')
        return value

    def calculate_cost(self, data):
        items = data.get('orderitem_set')
        subtotal, total_quantity = 0, 0
        for item in items:
            product = item.get('product')
            # if product is None:
            #     raise ParseError(f'Product with id {item.get("product")} does not exist!')
            quantity = int(item.get('quantity', 1))
            subtotal += (product.price * quantity)
            total_quantity += quantity
        return {
            'item_total': subtotal,
            'total_amount': subtotal + int(data.get('delivery_fee', 0)),
            'total_quantity': total_quantity
        }


class DailyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyData
        fields = ['created_date', 'total_amount', 'total_quantity']
