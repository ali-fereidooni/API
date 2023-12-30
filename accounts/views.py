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
from rest_framework import status
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

    def get(self, request):
        user = User.objects.all()
        srz_data = self.serializer_class(instance=user, many=True).data
        return Response(data=srz_data, status=status.HTTP_200_OK)


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
