# serializers.py

from rest_framework import serializers
from .models import AppUsers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUsers
        fields = ('username', 'email', 'password')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        fields=("email","password")

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print("inside the serializer")
        
            
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['user_id'] = user.id
        # token['is_active'] = user.is_active
        token['is_superuser'] = user.is_superuser
        # token['is_staff'] = user.is_staff
        return token
