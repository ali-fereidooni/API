from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserRegisterSerializer


class UserRegstrationView(APIView):
    def post(self, request):
        srz_data = UserRegisterSerializer(data=request.POST)
        if srz_data.is_valid():
            pass
