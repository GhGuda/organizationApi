from rest_framework import generics, status, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "status": "success",
                "message": "Registration successful",
                "data": {
                    "accessToken": AuthToken.objects.create(user)[1],
                    "user": UserSerializer(user).data
                }
            }, status=status.HTTP_201_CREATED)
        return Response({
            "errors": serializer.errors
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(email=serializer.data['email']).first()
            if user and user.check_password(serializer.data['password']):
                return Response({
                    "status": "success",
                    "message": "Login successful",
                    "data": {
                        "accessToken": AuthToken.objects.create(user)[1],
                        "user": UserSerializer(user).data
                    }
                }, status=status.HTTP_200_OK)
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