from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from PIL import Image


class CustomUserManager(BaseUserManager):
    def create_user(self, email: str, name: str, password: str, **extra_fields) -> AbstractBaseUser:
        if not email:
            raise ValueError("Email is required")

        if not password:
            raise ValueError("Password is required")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff_user(self, email: str, name: str, password: str, **extra_fields) -> AbstractBaseUser:
        extra_fields.setdefault("is_staff", True)

        return self.create_user(email, name, password, **extra_fields)

    def create_superuser(self, email: str, name: str, password: str, **extra_fields) -> AbstractBaseUser:
        extra_fields.setdefault("is_superuser", True)

        return self.create_staff_user(email, name, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
    quote = models.CharField(max_length=100, null=True, blank=True)
    registration_time = models.DateTimeField(verbose_name="Registered on:", auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self) -> str:
        return f"User {self.name} with email {self.email}"

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)

        if self.profile_picture:
            img = Image.open(self.profile_picture.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_picture.path)
