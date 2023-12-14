from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserRegisterSerializer


class UserRegstrationView(APIView):
    def post(self, request):
        srz_data = UserRegisterSerializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.create(srz_data.validated_data)
            return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
