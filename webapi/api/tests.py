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
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        assert 'result' in data
        products = data['result']
        assert len(products) == 2
