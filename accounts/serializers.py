from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id", "phone", "email", "author"
            "first_name", "last_name",
        ]


class AuthenticationSerializer(serializers.Serializer):
    phone = serializers.CharField(
        max_length=12,
        min_length=12,
    )

    def validate_phone(self, value):
        from re import match

        if not match("^989\d{2}\s*?\d{3}\s*?\d{4}$", value):
            raise serializers.ValidationError("Invalid phone number.")

        return value
