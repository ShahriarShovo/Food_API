from order.models.modifier import  Modifier
from rest_framework import serializers
from order.models.item import Item
from order.serializers.item_serializer import ItemSerializer

class ModifierSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    item_id = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(),
                                                    source='item', write_only=True)  # For writable item_id
    class Meta:
        model = Modifier
        fields = ['id', 'name', 'extra_price','item','item_id']