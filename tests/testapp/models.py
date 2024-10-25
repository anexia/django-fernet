from django.db import models

from django_fernet import fields as fernet_fields

__all__ = [
    "FernetTextModel",
    "FernetBinaryModel",
]


class FernetTextModel(models.Model):
    nullable = fernet_fields.FernetTextField(
        verbose_name="Nullable text",
        null=True,
        blank=True,
    )
    not_nullable = fernet_fields.FernetTextField(
        verbose_name="Not nullable text",
        null=False,
        blank=False,
    )


class FernetBinaryModel(models.Model):
    nullable = fernet_fields.FernetBinaryField(
        verbose_name="Nullable binary",
        null=True,
        blank=True,
    )
    not_nullable = fernet_fields.FernetBinaryField(
        verbose_name="Not nullable binary",
        null=False,
        blank=False,
    )
