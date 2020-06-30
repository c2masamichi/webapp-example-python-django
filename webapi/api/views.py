from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404

from api.models import Product


def get_products(request):
    products = Product.objects.all()
    data = {
        'result': [
            {
                'id': row.id,
                'name': row.name,
                'price': row.price,
            }
            for row in products
        ]
    }
    return JsonResponse(data)


def get_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    data = {
        'result': {
            'id': product.id,
            'name': product.name,
            'price': product.price,
        }
    }
    return JsonResponse(data)