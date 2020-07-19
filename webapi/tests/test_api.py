import json

import pytest

from api.models import Product

PATH_PREFIX = '/api/v1'


@pytest.mark.django_db
def test_get_products(client):
    path = '{0}/products'.format(PATH_PREFIX)
    response = client.get(path)
    assert response.status_code == 200

    data = json.loads(response.content)
    assert 'result' in data
    products = data['result']
    assert len(products) == 2
