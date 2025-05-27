from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from .backends import EmailBackend

UserModel = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password', 'phone_number')
        
    def validate_phone_number(self, value):
        # Validate 10-digit Indian phone number
        if len(value) != 10 or not value.isdigit():
            raise serializers.ValidationError('Phone number must be 10 digits (e.g., 9876543210)')
        return value
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number')
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(required=False)
    
    def validate(self, data):
        print(data)
        email = data.get('email')
        password = data.get('password')
        
        # Use our custom authentication backend
        backend = EmailBackend()
        user = backend.authenticate(
            request=self.context.get('request'),
            email=email,
            password=password
        )
        print(user)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['phone_number'] = instance.phone_number
        return representation
