from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *


urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    
]


urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="create-user"),
    path("login/", LoginAPI.as_view(), name="login-user"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("logout/", LogoutAPI.as_view(), name="logout-user"),
    path("", UserInfoAPI.as_view(), name="user-info"),
]
