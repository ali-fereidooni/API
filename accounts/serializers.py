from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('last_login', 'is_admin', 'is_active', 'is_superuser')
        extra_kwargs = {
            'password': {'write_only': True},
        }
