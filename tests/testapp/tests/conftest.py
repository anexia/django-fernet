import pytest

from django.core.management import call_command


@pytest.fixture()
def text_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "test_text.json")


@pytest.fixture()
def binary_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "test_binary.json")
