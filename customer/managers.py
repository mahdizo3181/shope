from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, phone, fullname, ):
        if not email:
            raise ValueError("users must have email")
        if not fullname:
            raise ValueError("users must have full name")
        if not phone:
            raise ValueError("users must have phone")

        user = self.model(email=self.normalize_email(email), fullname=fullname, phone=phone)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, phone, fullname):
        user = self.create_user(email, password, phone, fullname)
        user.is_admin = True
        user.save()
        return user
