import django_fernet.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FernetBinaryModel",
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
                    "nullable",
                    django_fernet.fields.FernetBinaryField(
                        blank=True,
                        null=True,
                        verbose_name="Nullable binary",
                    ),
                ),
                (
                    "not_nullable",
                    django_fernet.fields.FernetBinaryField(
                        verbose_name="Not nullable binary",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FernetTextModel",
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
                    "nullable",
                    django_fernet.fields.FernetTextField(
                        blank=True,
                        null=True,
                        verbose_name="Nullable text",
                    ),
                ),
                (
                    "not_nullable",
                    django_fernet.fields.FernetTextField(
                        verbose_name="Not nullable text",
                    ),
                ),
            ],
        ),
    ]
