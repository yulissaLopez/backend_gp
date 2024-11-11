from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
import uuid


# Create your models here.
# TO DO SEPARAR EN UN NUEVO ARCHIVO managers.py
""" Esta clase maneja como se crean y gestion los usuarios """
class UserManager(BaseUserManager):

    """le dice a django que este manager debe ser considerado durante las migraciones"""
    use_in_migrations = True

    # Metodo para crear un usuario normal
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Correo Obligatorio')
        
        if not password:
            raise ValueError('Contraseña Obligatoria')
        
        """
            self.model referencia el modelo de usuario (User().create_user)
            normalize_email es un metodo de BaseUserManager que se asegura que el correo 
            este en un formato standar
            **extra_fields es un diccionario de campos adicionales que se pueden pasar al crear
            un usuario 
        """
        
        user = self.model(email=self.normalize_email(email), **extra_fields)

        # Encripta la contraseña
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('el atributo is_staff debe ser True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('el atributo is_superuser debe ser True')
        
        return self.create_user(email, password, **extra_fields)

# MODELO  
class CustomUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=False)
    email = models.EmailField(max_length=100, unique=True, error_messages={'unique': "Este correo electrónico ya está registrado."})
    # TO DO REVISAR ESTE CAMPO PARA VERIFICACION DE USUARIO DE A TRAVES DEL CORREO
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)


    """ Le indica a django que se usara el email en lugar del username en la autenticacion"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    """indica que utilice el UserManager para interactuar con las instancias del modelo"""
    objects = UserManager()

    def __str__(self) :
        return self.email

#REVISAR EL USO DE BASEABSTRACTUSER