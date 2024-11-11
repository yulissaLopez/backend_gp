from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "name", 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        print('Hey')
        # Normalize the email to lowercase for consistent validation
        norm_email = value.lower()
        # Perform a case-insensitive check for existing email
        if CustomUser.objects.filter(email__iexact=norm_email).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
        
        return norm_email

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
