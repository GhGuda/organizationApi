from django.urls import path
from .views import RegisterAPI, LoginAPI
from .views import UserDetailAPI


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('users/<int:pk>/', UserDetailAPI.as_view(), name='user-detail'),
    path('login/', LoginAPI.as_view(), name='login'),
]
