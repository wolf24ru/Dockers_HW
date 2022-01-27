import pytest
from rest_framework.status import HTTP_200_OK


def test_something():
    assert True


@pytest.mark.django_db
def test_pig(client):
    url = 'http://localhost:8000/api/v1/'
    resp = client.get(url)
    assert resp.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_create_product(client, url, product_factory):
    product = product_factory(_quantity=2)
    url += f'{product[0].id}/'

    response = client.get(url)

    assert response.status_code == HTTP_200_OK
