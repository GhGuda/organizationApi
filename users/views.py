from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework.exceptions import ValidationError

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            accessToken = str(refresh.access_token)
            return Response({
                "status": "success",
                "message": "Registration successful",
                "data": {
                    "accessToken": accessToken,
                    "user": UserSerializer(user).data
                }
            }, status=status.HTTP_201_CREATED)
            
        except ValidationError as error:
            return Response({
                "errors": error.detail
            }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        except:
            return Response(
                {
                    "status": "Bad request",
                    "message": "Registration unsuccessful",
                    "statusCode": 400
                }, status=status.HTTP_400_BAD_REQUEST

            )

class LoginAPI(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response({
                    "status": "success",
                    "message": "Login successful",
                    "data": serializer.validated_data
                }, status=status.HTTP_200_OK)
        except:
            return Response({
                "status": "Bad request",
                "message": "Authentication failed",
                "statusCode": 401
            }, status=status.HTTP_401_UNAUTHORIZED)
            



class UserDetailAPI(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response({
            "status": "success",
            "message": "User details retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)