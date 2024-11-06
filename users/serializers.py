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
        print(norm_email, value)
        # TO DO REVISAR
        if CustomUser.objects.filter(email=norm_email).exists():
            raise serializers.ValidationError("Este correo electrónico ya está registrado.")
        
        return norm_email

    def create(self, validated_data):
        email = validated_data['email']
        validated_data['email']=email.lower()

        print(validated_data['email'])
        try:
            user = CustomUser.objects.create_user(email=validated_data['email'],
                                                name=validated_data['name'],
                                                password=validated_data['password'])
            return user
        except IntegrityError:
            self.fail("email", "Este correo electrónico ya está registrado.")

    
    