# Generated by Django 5.0.2 on 2024-03-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="users",
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
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("is_anonymous", models.BooleanField(default=False)),
                ("is_authenticated", models.BooleanField(default=False)),
                ("date_of_birth", models.DateField(default="0000-00-00")),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("username", models.CharField(max_length=255, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255, unique=True)),
            ],
            options={
                "ordering": ("-username",),
            },
        ),
    ]