from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.conf import settings
import uuid

#Extend BaseUserManager to create  Custom User Manager
class MyUserManager(BaseUserManager):
    
    #create a user
    def create_user(self, email, password=None, **extra_fields):
        #email check
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email) #email normalize
        user = self.model(email=email, **extra_fields) #creating user
        user.set_password(password)#creating password
        user.save(using=self._db)# finally saved to database
        return user

    # This function will create super user
    def create_superuser(self, email, password, **extra_fields):
        #set super user extra fields
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # checking extra fields and having issue or not
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True')

        return self.create_user(email, password, **extra_fields)