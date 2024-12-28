from rest_framework import serializers
from user.models import User
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenRefreshView


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):


    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer


    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model= User
        fields=['username','email','name','last_name']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model= User
        fields= '__all__'

    def create(self, validated_data):
        user= User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        update_user=super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields ='__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }