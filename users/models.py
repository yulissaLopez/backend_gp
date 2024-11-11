from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser
import uuid

# Create your models here.
# MODELO  
class CustomUser(AbstractBaseUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=False)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # TODO REVISAR ESTE CAMPO PARA VERIFICACION DE USUARIO DE A TRAVES DEL CORREO
    # is_verified = models.BooleanField(default=False)

    # Indica que utilice el UserManager para interactuar con las instancias del modelo
    objects = UserManager()

    # Indica a django que se usara el email en lugar del username en la autenticacion
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # Al imprimir el objecto se mostrara el valor de name en lugar de la representacion predeterminada del objeto
    def __str__(self) :
        return self.name
