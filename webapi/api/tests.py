import json

from django.urls import reverse
from django.test import TestCase

from api.models import Product


class ProductsViewTests(TestCase):
    def setUp(self):
        Product.objects.create(name='book', price=600)
        Product.objects.create(name='fish', price=200)

    def test_get_products(self):
        response = self.client.get(reverse('api_v1:list'))
        assert response.status_code == 200

        data = json.loads(response.content)
        assert 'result' in data
        products = data['result']
        assert len(products) == 2

    def test_get_product(self):
        product_id = 1
        name = 'book'
        price = 600
        url = reverse('api_v1:detail', args=(product_id,))
        response = self.client.get(url)
        assert response.status_code == 200

        data = json.loads(response.content)
        assert 'result' in data
        product = data['result']
        assert product['id'] == product_id
        assert product['name'] == name
        assert product['price'] == price

    def test_get_product_exists_required(self):
        product_id = 10
        url = reverse('api_v1:detail', args=(product_id,))
        response = self.client.get(url)
        assert response.status_code == 404

    def test_create_product(self):
        name = 'meet'
        price = 1000
        new_product = {
            'name': name,
            'price': price,
        }
        url = reverse('api_v1:create')
        response = self.client.post(url, new_product)
        assert response.status_code == 200

        product = Product.objects.get(pk=3)
        assert product.name == name
        assert product.price == price