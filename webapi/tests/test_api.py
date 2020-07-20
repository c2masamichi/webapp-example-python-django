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


@pytest.mark.django_db
def test_get_product(client):
    product_id = 1
    name = 'book'
    price = 600
    path = '{0}/products/{1}'.format(PATH_PREFIX, product_id)
    response = client.get(path)
    assert response.status_code == 200

    data = json.loads(response.content)
    assert 'result' in data
    product = data['result']
    assert product['id'] == product_id
    assert product['name'] == name
    assert product['price'] == price


@pytest.mark.django_db
def test_get_product_exists_required(client):
    path = '{0}/products/10'.format(PATH_PREFIX)
    response = client.get(path)
    assert response.status_code == 404


@pytest.mark.django_db
def test_create_product(client):
    post_data = {
        'name': 'meet',
        'price': 1000,
    }
    path = '{0}/products'.format(PATH_PREFIX)
    response = client.post(
        path, data=post_data,
        content_type='application/json'
    )
    assert response.status_code == 200

    product = Product.objects.get(pk=3)
    assert product.name == post_data['name']
    assert product.price == post_data['price']


@pytest.mark.django_db
def test_create_product_validate01(client):
    path = '{0}/products'.format(PATH_PREFIX)
    response = client.post(path, data={'data': 'wrong data'})
    assert response.status_code == 400
    data = json.loads(response.content)
    assert 'Content-Type must be application/json.' in data['error']


@pytest.mark.django_db
def test_update_product(client):
    product_id = 2
    post_data = {
        'name': 'rice',
        'price': 900,
    }
    path = '{0}/products/{1}'.format(PATH_PREFIX, product_id)
    response = client.put(
        path, data=post_data,
        content_type='application/json'
    )
    assert response.status_code == 200

    product = Product.objects.get(pk=product_id)
    assert product.name == post_data['name']
    assert product.price == post_data['price']


@pytest.mark.django_db
def test_update_product_exists_required(client):
    post_data = {
        'name': 'rice',
        'price': 900,
    }
    path = '{0}/products/10'.format(PATH_PREFIX)
    response = client.put(
        path, data=post_data,
        content_type='application/json'
    )
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_product_validate01(client):
    product_id = 2
    path = '{0}/products/{1}'.format(PATH_PREFIX, product_id)
    response = client.put(path, data={'data': 'wrong data'})
    assert response.status_code == 400
    data = json.loads(response.content)
    assert 'Content-Type must be application/json.' in data['error']


@pytest.mark.django_db
def test_delete_product(client):
    product_id = 2
    path = '{0}/products/{1}'.format(PATH_PREFIX, product_id)
    response = client.delete(path)
    assert response.status_code == 200

    with pytest.raises(Product.DoesNotExist):
        Product.objects.get(pk=product_id)


@pytest.mark.django_db
def test_delete_product_exists_required(client):
    path = '{0}/products/10'.format(PATH_PREFIX)
    response = client.delete(path)
    assert response.status_code == 404
