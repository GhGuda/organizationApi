from django.urls import path
from .views import RegisterAPI, LoginAPI


urlpatterns = [
    path('auth/register/', RegisterAPI.as_view(), name='register'),
    path('auth/login/', LoginAPI.as_view(), name='login'),
]
