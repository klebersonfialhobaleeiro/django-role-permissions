from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(AbstractUser):
    choice_cargo = (
        ('S', 'Secretaria'),
        ('M', 'Medico'),
        ('P', 'Paciente')
    )
    cargo = models.CharField(max_length=1, choices=choice_cargo)