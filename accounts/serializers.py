from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        exclude = ('last_login', 'is_admin', 'is_active', 'is_superuser')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)
