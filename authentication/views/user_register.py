from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from authentication.serializers.user_register_serializer import RegisterSerializer
from authentication.serializers.user_token_serializer import UserTokenSerializer



#Function based view
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data) #serializer for user input
    if serializer.is_valid():
        user = serializer.save()  # user saved and  token created
        token_data = UserTokenSerializer(user.usertoken).data  # Serialize token data
        return Response(token_data, status=status.HTTP_201_CREATED) # return if user is created
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)# return if if user is not created