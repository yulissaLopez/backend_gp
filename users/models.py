from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
# MODELO  
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
    # TO DO REVISAR ESTE CAMPO PARA VERIFICACION DE USUARIO DE A TRAVES DEL CORREO
    is_verified = models.BooleanField(default=False)

    """indica que utilice el UserManager para interactuar con las instancias del modelo"""
    objects = UserManager()

    """ Le indica a django que se usara el email en lugar del username en la autenticacion"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self) :
        return self.name

#REVISAR EL USO DE BASEABSTRACTUSER