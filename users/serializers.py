from rest_framework import serializers
from .models import CustomUser
from django.db import IntegrityError

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        """Campos que se incluyen en el serializador"""
        fields = ["id", "email", "name", 'password']
        extra_kwargs = {'password': {'write_only': True}}

    
    def validate_email(self, value):
        # Covierte el email a LowerCase
        norm_email = value.lower()

        # TO DO REVISAR
        if CustomUser.objects.filter(email=norm_email).exists():
            raise serializers.ValidationError("Este correo electrónico ya está registrado.")
        
        return norm_email

    def create(self, validated_data):
        print(validated_data['email'])
        user = CustomUser.objects.create_user(validated_data['email'],
                                            name = validated_data['name'],
                                            password = validated_data['password'])
        return user
    
    