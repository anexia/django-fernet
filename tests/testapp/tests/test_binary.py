import pytest

from django_fernet.fernet import *

from testapp.models import *


@pytest.mark.django_db(transaction=True)
def test_simple_safe_and_load():
    field_value_1 = FernetBinaryFieldData()
    field_value_1.encrypt(b"foo", "--secret--")

    field_value_2 = FernetBinaryFieldData()
    field_value_2.encrypt(b"bar", "--secret--")

    instance = FernetBinaryModel()
    instance.nullable = field_value_1
    instance.not_nullable = field_value_2
    instance.save()

    loaded_instance = FernetBinaryModel.objects.get(pk=instance.pk)

    assert loaded_instance.nullable.decrypt("--secret--") == b"foo"
    assert loaded_instance.not_nullable.decrypt("--secret--") == b"bar"


@pytest.mark.django_db(transaction=True)
def test_load_fixture_data(binary_fixtures):
    loaded_instance = FernetBinaryModel.objects.get(pk=1)

    assert loaded_instance.nullable.decrypt("--secret--") == b"fixture:foo"
    assert loaded_instance.not_nullable.decrypt("--secret--") == b"fixture:bar"
