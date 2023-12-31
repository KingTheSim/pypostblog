# Generated by Django 4.2.7 on 2023-11-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("name", models.CharField(max_length=30)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="profile_pics/"),
                ),
                ("quote", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "registration_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Registered on:"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
