from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from authentication.models import UserToken
from authentication.serializers.user_serializer import UserSerializer
from authentication.serializers.user_token_serializer import UserTokenSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email') #input email 
    password = request.data.get('password')#input password

    #checking if email or password is empty or both is empty
    if email is None or password is None:
        return Response({'error': 'Please provide both email and password.'}, status=status.HTTP_400_BAD_REQUEST)

    #authenticate user email and password
    user = authenticate(request, email=email, password=password)

    #if user is not empty than it will check user token is exist or not 
    # if not exist than it will create one 
    if user is not None:
        try:
            token = UserToken.objects.get(user=user)
        except UserToken.DoesNotExist:
            token = UserToken.objects.create(user=user)
        
        #get user data
        user_data = UserSerializer(user).data
        #print(user_data)
        #get user data and token
        token_data = UserTokenSerializer(token).data
        #print(token_data)
        #return user data and token 
        return Response({**user_data, 'token': token_data['token']}, status=status.HTTP_200_OK)
    
    # if user email or password is match or user is not exists 
    else:
        return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

