from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password')
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        print(data)
        user = authenticate(
            request=self.context.get('request'),
            email=data.get('email'),
            password=data.get('password')
        )
        print(user)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
