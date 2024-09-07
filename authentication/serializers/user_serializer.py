from rest_framework import serializers
from authentication.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # custom User model
        fields = ['id', 'email']  # 'username' is not a field in custom User model