from rest_framework import serializers
from authentication.models.user import User
from authentication.models.user_token import UserToken

class RegisterSerializer(serializers.ModelSerializer):
    # get confirm password for matching
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User  #custom User model
        fields = ['email', 'password', 'confirm_password'] 
        extra_kwargs = {'password': {'write_only': True}}

    # password validate , user password match with confirm password or not
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    # create a new user with validated data
    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password from validated_data
        user = User.objects.create_user(**validated_data) # create user
        UserToken.objects.create(user=user) # create token with user
        return user