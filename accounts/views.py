from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
import random
from .serializers import UsersListSerializer
from utils import send_otp_code


class UserList(APIView):
    """
    get:
        Returns a list of all existing users
    """
    serializer_class = UsersListSerializer
