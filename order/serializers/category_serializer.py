from order.models.category import Category
from rest_framework import serializers

# Assuming Category has a ForeignKey to Menu
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','description', 'menu']  # Make sure 'menu' is included