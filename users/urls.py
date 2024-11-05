from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, UserList
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    # TokenObtainPairView
)

urlpatterns = [
    path('', UserList.as_view(), name='user_list'),
    path('register/', RegisterView.as_view(), name = "sign_up"),
    #Authentication
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]