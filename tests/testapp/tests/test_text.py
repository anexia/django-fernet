import pytest

from django_fernet.fernet import *

from testapp.models import *


@pytest.mark.django_db(transaction=True)
def test_simple_safe_and_load():
    field_value_1 = FernetTextFieldData()
    field_value_1.encrypt("foo", "--secret--")

    field_value_2 = FernetTextFieldData()
    field_value_2.encrypt("bar", "--secret--")

    instance = FernetTextModel()
    instance.nullable = field_value_1
    instance.not_nullable = field_value_2
    instance.save()

    loaded_instance = FernetTextModel.objects.get(pk=instance.pk)

    assert loaded_instance.nullable.decrypt("--secret--") == "foo"
    assert loaded_instance.not_nullable.decrypt("--secret--") == "bar"


@pytest.mark.django_db(transaction=True)
def test_load_fixture_data(text_fixtures):
    loaded_instance = FernetTextModel.objects.get(pk=1)

    assert loaded_instance.nullable.decrypt("--secret--") == "fixture:foo"
    assert loaded_instance.not_nullable.decrypt("--secret--") == "fixture:bar"
