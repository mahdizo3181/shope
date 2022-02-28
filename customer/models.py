from django.db import models
from django.db.models import Model
from django.utils.translation import gettext_lazy as _
from social_core.backends import username

from core.models import BaseModel
from django.contrib.auth.models import AbstractUser
from .managers import MyUserManager


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=16)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name', ]

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)


class Address(BaseModel):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    City = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    home_plate = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created}'
