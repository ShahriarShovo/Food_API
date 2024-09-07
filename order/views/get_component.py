from django.shortcuts import render
from functools import wraps
from rest_framework.decorators import api_view
from rest_framework.response import Response
from order.models.menu import Menu
from order.models.category import Category
from order.models.item import Item
from order.models.modifier import  Modifier
from order.serializers.menu_serializer import MenuSerializer
from order.serializers.category_serializer import CategorySerializer
from order.serializers.item_serializer import ItemSerializer
from order.serializers.modifier_serializer import ModifierSerializer
from rest_framework.decorators import api_view

# This is a normal function based view for get category, item, modifier and menu
'''
@api_view(['GET'])
def menu_list(request):
    menus = Menu.objects.all()
    serializer = MenuSerializer(menus, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def modifier_list(request):
    modifiers = Modifier.objects.all()
    serializer = ModifierSerializer(modifiers, many=True)
    return Response(serializer.data)

'''


# used here decorator for same work
def list_view(model, serializer_class):
    # inner function
    def decorator(func):
        @wraps(func)
        @api_view(['GET'])  # Apply the api_view decorator
        #another inner function
        def wrapped_view(request, *args, **kwargs):
            # Fetch all objects for the provided model
            objects = model.objects.all()
            # Serialize the objects
            serializer = serializer_class(objects, many=True)
            return Response(serializer.data)
        return wrapped_view
    return decorator


# Menu List
@list_view(Menu, MenuSerializer)
def menu_list(request):
    pass

# Category List
@list_view(Category, CategorySerializer)
def category_list(request):
    pass

# Item List
@list_view(Item, ItemSerializer)
def item_list(request):
    pass

# Modifier List
@list_view(Modifier, ModifierSerializer)
def modifier_list(request):
    pass