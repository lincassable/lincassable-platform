import pytest


@pytest.fixture()
def anon_client():
    """A Django anonymous client."""
    from django.test.client import Client

    return Client()
