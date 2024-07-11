from rest_framework import serializers
from .models import User
from organisations.models import Organisation
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'firstName', 'lastName', 'email', 'phone']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email', 'password', 'phone']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Organisation.objects.create(name=f"{user.firstName}'s Organisation")
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class CustomObtainTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        accessToken = str(refresh.access_token)
        user = UserSerializer(instance=self.user)
        
        data ={
            "accessToken": accessToken,
            "user": {
                "userId": user.userId,
                "firstName": user.firstName,
				"lastName": user.lastName,
				"email": user.email,
				"phone": user.phone,
            }
        }
        
        return data            
      
      