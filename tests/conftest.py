import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def url():
    return 'http://localhost:8000/api/v1/products/'


@pytest.fixture
def product_factory():
    def factory(**kwargs):
        return baker.make('Product', **kwargs)
    return factory
