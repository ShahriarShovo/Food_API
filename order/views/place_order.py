from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from order.serializers.order_serializer import OrderSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure user is authenticated
def place_order(request):
    serializer = OrderSerializer(data=request.data, context={'request': request})  # Pass request to context
    if serializer.is_valid():
        order = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)