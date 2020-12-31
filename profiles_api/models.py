from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):

    def create_user(self,email,name,country,city,address,password=None):

        if not email:
            raise ValueError('Users must have email address')

        email = self.normalize_email(email)
        user =  self.model(email=email,name=name,country=country,city=city,address=address)


        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,country,city,address,password):

        user = self.create_user(email,name,country,city,address,password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)

        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    country_id = models.ForeignKey('Country',on_delete=models.CASCADE, null=True)
    city_id = models.ForeignKey('City',on_delete=models.CASCADE, null=True)
    address_id = models.ForeignKey('Address',on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','country','city','address']

    def get_full_name(self):

        return self.name
    def get_short_name(self):

        return self.name

    def __str__(self):
        return self.email

class Country(models.Model):
    name = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

class Address(models.Model):
    name = models.CharField(max_length=70)

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

class ProfileFeedItem(models.Model):

    user_profile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text