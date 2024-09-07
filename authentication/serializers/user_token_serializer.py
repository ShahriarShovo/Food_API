from rest_framework import serializers
from authentication.serializers.user_serializer import UserSerializer
from authentication.models.user_token import UserToken

# create user token with user
class UserTokenSerializer(serializers.ModelSerializer):
    user = UserSerializer() # call user serializer for user information
    class Meta:
        model = UserToken
        fields = ['user', 'token']