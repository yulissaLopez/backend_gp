from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import CustomUser

# Create your views here.
class RegisterView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

# Para Logearse  
# TO DO CUSTOM TOKEN  
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
        except AuthenticationFailed:
            raise AuthenticationFailed("Las credenciales proporcionadas no son correctas.")
        return response

class UserList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format = None):
        user = CustomUser.objects.all()
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
