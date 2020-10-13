from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    "Admin para Perfiles de Usuarios"
    def create_user(self, email, name, password= None):
        "Crear Nuevo Perfil de Usuario"
        if not email:
            raise ValueError('Ingrese un Mail de usuario')
        
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    "Modelo BD para users en el sistema"
    email = models.EmailField(max_length=200, unique= True)
    name = models.Charfield(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        "Obtener nombre Completo"
        return self.name

    def get_short_name(self):
        "Obtener nombre Corto del Usuario"
        return self.name

    def __str__(self):
        return self.email