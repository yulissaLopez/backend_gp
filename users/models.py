from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid

# Create your models here.

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
    
class CustomUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    name = models.CharField(max_length=100, unique=False)

    email = models.EmailField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default= False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    """indica que utilice el UserManager para interactuar con las instancias del modelo"""
    objects = UserManager()

    """ Le indica a django que se usara el email en lugar del username en la autenticacion"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self) :
        return self.name