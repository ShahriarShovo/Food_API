from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin
from authentication.models.my_user_manager import MyUserManager

# Custom User Model
# Extend AbstractBaseUser and PermissionsMixin class for creating an user

class User(AbstractBaseUser, PermissionsMixin):
    
    #Define owner, employee and customers
    OWNER = 'owner'
    EMPLOYEE = 'employee'
    CUSTOMER = 'customer'

    # Role choices 
    ROLE_CHOICES = [
        (OWNER, 'Owner'),
        (EMPLOYEE, 'Employee'),
        (CUSTOMER, 'Customer'),
    ]
    
    email = models.EmailField(unique=True, null=False)
    
    # staff status
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log in this site'),
    )
    # active  status
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts'),
    )
    
    
    # set user role
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CUSTOMER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # create user object
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email