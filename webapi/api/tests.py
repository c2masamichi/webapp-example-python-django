import json

from django.test import TestCase

from api.models import Product

PATH_PREFIX = '/api/v1'


class ProductsViewTests(TestCase):
    def setUp(self):
        Product.objects.create(name='book', price=600)
        Product.objects.create(name='fish', price=200)

    def test_get_products(self):
        path = '{0}/products'.format(PATH_PREFIX)
        response = self.client.get(path)
        assert response.status_code == 200

        data = json.loads(response.content)
        assert 'result' in data
        products = data['result']
        assert len(products) == 2

    def test_get_product(self):
        product_id = 1
        name = 'book'
        price = 600
        path = '{0}/products/{1}'.format(PATH_PREFIX, product_id)
        response = self.client.get(path)
        assert response.status_code == 200

        data = json.loads(response.content)
        assert 'result' in data
        product = data['result']
        assert product['id'] == product_id
        assert product['name'] == name
        assert product['price'] == price

    def test_get_product_exists_required(self):
        path = '{0}/products/10'.format(PATH_PREFIX)
        response = self.client.get(path)
        assert response.status_code == 404

    def test_create_product(self):
        post_data = {
            'name': 'meet',
            'price': 1000,
        }
        path = '{0}/products'.format(PATH_PREFIX)
        response = self.client.post(
            path, data=post_data,
            content_type='application/json'
        )
        assert response.status_code == 200

        product = Product.objects.get(pk=3)
        assert product.name == post_data['name']
        assert product.price == post_data['price']

    def test_create_product_validate01(self):
        path = '{0}/products'.format(PATH_PREFIX)
        response = self.client.post(path, data={'data' :'wrong data'})
        assert response.status_code == 400
        data = json.loads(response.content)
        assert 'Content-Type must be application/json.' in data['error']

    def test_update_product(self):
        product_id = 2
        post_data = {
            'name': 'rice',
            'price': 900,
        }
        path = '{0}/products/{1}'.format(PATH_PREFIX, product_id)
        response = self.client.put(
            path, data=post_data,
            content_type='application/json'
        )
        assert response.status_code == 200

        product = Product.objects.get(pk=product_id)
        assert product.name == post_data['name']
        assert product.price == post_data['price']

    def test_update_product_exists_required(self):
        post_data = {
            'name': 'rice',
            'price': 900,
        }
        path = '{0}/products/10'.format(PATH_PREFIX)
        response = self.client.put(
            path, data=post_data,
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_update_product_validate01(self):
        product_id = 2
        path = '{0}/products/{1}'.format(PATH_PREFIX, product_id)
        response = self.client.put(path, data={'data' :'wrong data'})
        assert response.status_code == 400
        data = json.loads(response.content)
        assert 'Content-Type must be application/json.' in data['error']

    def test_delete_product(self):
        product_id = 2
        path = '{0}/products/{1}'.format(PATH_PREFIX, product_id)
        response = self.client.delete(path)
        assert response.status_code == 200

        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(pk=product_id)

    def test_delete_product_exists_required(self):
        path = '{0}/products/10'.format(PATH_PREFIX)
        response = self.client.delete(path)
        assert response.status_code == 404
