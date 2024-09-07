from django.shortcuts import render
from functools import wraps
from rest_framework.decorators import api_view
from rest_framework.response import Response
from order.serializers.menu_serializer import MenuSerializer
from order.serializers.category_serializer import CategorySerializer
from order.serializers.item_serializer import ItemSerializer
from order.serializers.modifier_serializer import ModifierSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from authentication.permissions import IsOwnerOrEmployee


# Used decorator to create category, menu, modifier and item
def create_object(serializer_class):
    #inner function
    def decorator(func):
        @wraps(func)
        @api_view(['POST'])
        @permission_classes([IsOwnerOrEmployee]) # custom permisson only owner or employee
        # inside another inner function
        def wrapped_view(request, *args, **kwargs):
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return wrapped_view
    return decorator


# Create Manue
@create_object(MenuSerializer)
def create_menu(request):
    pass

# Create Category
@create_object(CategorySerializer)
def create_category(request):
    pass

# Create Item
@create_object(ItemSerializer)
def create_item(request):
    pass

# Create Modifier
@create_object(ModifierSerializer)
def create_modifier(request):
    pass



# This is normal function based view for create category, item, menu and modifier

'''
@api_view(['POST'])
@permission_classes([IsOwnerOrEmployee])
def create_menu(request):
    serializer = MenuSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsOwnerOrEmployee])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsOwnerOrEmployee])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsOwnerOrEmployee])
def create_modifier(request):
    serializer = ModifierSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''