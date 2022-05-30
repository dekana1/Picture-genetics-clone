from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("email is required")
        if not first_name:
            raise ValueError("first name is required")
        if not last_name:
            raise ValueError("last name is required")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=60, unique=True)
    first_name = models.CharField(verbose_name='First name', max_length=200)
    last_name = models.CharField(verbose_name='Last name', max_length=200)

    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='date joined')
    last_login = models.DateTimeField(verbose_name='Last login', auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    object = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

# class AccountInfo(models.Model):
#     SexType = models.TextChoices('SexType', 'Male Female')
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     genetic_sex = models.CharField(blank=True, choices=SexType.choices, max_length=10)
#     date_of_birth = models.DateField(default=timezone.now)
#     phone = models.IntegerField(default=200)
#     address = models.CharField(max_length=500, default="332, kusa Jisalo")
#     city = models.CharField(max_length=200, default="Apo-resettlement")
#     state = models.CharField(max_length=200, default="Abuja")
#     postal_code = models.IntegerField(default=20000)
#     country = models.CharField(max_length=200, default="Nigeria")
#     language = models.CharField(max_length=200, default="English, US")
