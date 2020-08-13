from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.



class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password):
        if not email:
            return ValueError("Ingrese un email")
        if not username :
            return ValueError("Ingrese un Username ")
        user = self.model(
            email= self.normalize_email(email),
            username = username,
        )

        print(password)
        user.set_password(password)
        user.password
        print('usuario')
        print(user.password)
        user.save(using=self._db)
        user.save()
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
      #  user.set_password(password)
        print(user.password)
        print('superUsuario')
        user.password
        user.is_admin=True
        user.is_staff = True
        user.is_superuser = True
        user.save(using= self._db)
        return user

class Account (AbstractBaseUser):
    email = models.EmailField(max_length=50,unique=True)
    username = models.CharField(max_length=50,unique=True)
    date_joined= models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    #first_name = models.CharField(max_length=50)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm , obj=None):
        return self.is_admin

    def has_module_perms(self,app_Label):
        return True

