from rest_framework import serializers
from order.models.item import Item
from order.models.order import Order

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), many=True)  # Accepts list of item IDs
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # Don't accept user from input, it's set from request

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_amount', 'payment_method', 'is_paid', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user  # Get the authenticated user from the request context
        order = Order.objects.create(user=user, **validated_data)
        order.items.set(items_data)  # Set the many-to-many items field
        return order