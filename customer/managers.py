from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, phone, first_name, last_name):
        if not email:
            raise ValueError("users must have email")
        if not first_name:
            raise ValueError("users must have first name")
        if not last_name:
            raise ValueError("users must have last name")
        if not phone:
            raise ValueError("users must have phone")

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name, phone=phone)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, phone, first_name, last_name):
        user = self.create_user(email, password, phone, first_name, last_name)
        user.is_admin = True
        user.save()
        return user
