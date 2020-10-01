from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email,
                    phone_number,
                    username=None,
                    password=None,
                    is_active=True,
                    is_staff=False,
                    is_admin=False,
                    ):
        if not phone_number:
            raise ValueError("Unique Phone Number is required")
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("Password is required")
        user_obj = self.model(
            email=email
        )
        user_obj.set_password(password)  # change user password
        user_obj.username = 'admin-angga-4'
        user_obj.phone_number = phone_number
        user_obj.email = email
        user_obj.staff = True
        user_obj.admin = True
        user_obj.is_admin = True
        user_obj.is_staff = True
        user_obj.is_superuser = True
        user_obj.active = True
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self,email,phone_number,username=None,password=None):
        user = self.create_user(
            username=phone_number,
            phone_number=phone_number,
            email=email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user