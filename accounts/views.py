from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, OtpCode
import random
from .serializers import UserRegisterSerializer, UserVerifyCode
from utils import send_otp_code


class UserRegstrationView(APIView):

    def post(self, request):
        """
        create new user
        """
        srz_data = UserRegisterSerializer(data=request.POST)
        if srz_data.is_valid():
            random_code = random.randint(0000, 9999)
            send_otp_code(srz_data.validated_data['phone_number'], random_code)
            OtpCode.objects.create(
                phone_number=srz_data.validated_data, code=random_code)
            return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserVerifyView(APIView):
    def post(self, request):
        """
        Verify registered view
        """
        code_instance = OtpCode.objects.get()
        srz_data = UserVerifyCode(request.POST)
        if srz_data.is_valid():
            pass
