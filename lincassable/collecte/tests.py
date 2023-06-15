import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_points_de_collecte(anon_client):
    res = anon_client.get(reverse("index"))
    assert res.status_code == 200
