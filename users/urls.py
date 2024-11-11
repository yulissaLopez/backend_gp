from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import CustomUser
from users.serializers import UserSerializer
from .views import RegisterView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    # TokenObtainPairView
)
from rest_framework.generics import CreateAPIView

urlpatterns = [
    path(
        'register/',
        CreateAPIView.as_view(
            queryset=CustomUser.objects.all(),
            serializer_class=UserSerializer
        ),
        name='sign_up'
    ),
    #Authentication
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]