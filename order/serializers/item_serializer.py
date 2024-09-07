from order.models.item import Item
from rest_framework import serializers
from order.serializers.category_serializer import CategorySerializer
from order.models.category import Category


class ItemSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer(read_only=True)  # For nested category display
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
                                                    source='category', write_only=True)  # For writable category_id
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'available', 'category', 'category_id']
