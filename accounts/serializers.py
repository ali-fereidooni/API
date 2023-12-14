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

    def update(self, validated_data):
        del validated_data['password2']
        return User.objects.update(**validated_data)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('passwords must match')
        return data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.validated_data['password'])
        if commit:
            user.save()
        return user
