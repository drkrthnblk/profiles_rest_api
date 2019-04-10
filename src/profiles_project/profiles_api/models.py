from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """
        helps django to work with our custom user model
    """

    def create_user(self, email, name, password=None):
        """
            creates a new user profile object
        """
        if not email:
            raise ValueError("Users must have an email address")

        # normalizing email address -> converts all chars to lowercase
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.ser_password(password)
        
        user.save(using=self.db)
        return user

    def create_super_user(self, email, name, password):
        """
            creates and saves a superuser with given details
        """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self.db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
        Represent a user profile inside our system
    """
    email = models.EmailField(max_length=2255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
            Used to get a users full name
        """
        return self.name

    def get_short_name(self):
        """
            Used to get a users short name
        """
        return self.name

    def __str__(self):
        """
            django uses this to convert object to string
        """
        return self.email
