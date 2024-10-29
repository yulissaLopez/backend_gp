from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class User(AbstractUser):
    # id con uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    