from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import User
import random
from .serializers import (
    UsersListSerializer,
    UserDetailUpdateDeleteSerializer,
)
from utils import send_otp_code
from psermissions import IsSuperUser
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


class UserList(APIView):
    """
    get:
        Returns a list of all existing users
    """
    serializer_class = UsersListSerializer
    permission_classes = [IsSuperUser,]
    filterset_fields = [
        "author",
    ]
    search_fields = [
        "phone",
        "first_name",
        "last_name",
    ]
    ordering_fields = (
        "id", "author",
    )

    def get_queryset(self):
        return get_user_model().objects.values(
            'id', 'phone', 'first_name', 'last_name', 'author'
        )


class UserDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns the detail of a user instance.

        parameters: [pk]

    put:
        Update the detail of a user instance

        parameters: exclude[password,]

    delete:
        Delete a user instance.

        parameters: [pk]
    """

    serializer_class = UserDetailUpdateDeleteSerializer
    permission_classes = [
        IsSuperUser,
    ]

    def get_object(self):
        pk = self.kwargs.get("pk")
        user = get_object_or_404(User.objects.defer(
            "password",
        ),
            pk=pk
        )
        return user
