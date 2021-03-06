import json

from django.core.exceptions import ValidationError
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods

from api.models import Product


@require_http_methods(['GET', 'POST'])
def list_or_create_product(request):
    if request.method == 'GET':
        return get_products(request)
    elif request.method == 'POST':
        return create_product(request)


@require_http_methods(['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_product(request, product_id):
    if request.method == 'GET':
        return get_product(request, product_id)
    elif request.method == 'PUT':
        return update_product(request, product_id)
    elif request.method == 'DELETE':
        return delete_product(request, product_id)


def get_products(request):
    products = Product.objects.all()
    data = {
        'result': [
            {
                'id': product.id,
                'name': product.name,
                'price': product.price,
            }
            for product in products
        ]
    }
    return JsonResponse(data)


def create_product(request):
    if request.headers.get('Content-Type') != 'application/json':
        data = {
            'error': 'Bad Request: Content-Type must be application/json.'
        }
        return JsonResponse(data, status=400)

    body = json.loads(request.body)
    name = body.get('name')
    price = body.get('price')
    if name is None or price is None:
        data = {
            'error': 'Bad Request: The key "name" and "price" are required.'
        }
        return JsonResponse(data, status=400)

    try:
        product = Product(name=name, price=price)
        product.full_clean()
        product.save()
    except ValidationError:
        data = {
            'error': 'Bad Request: Bad data.'
        }
        return JsonResponse(data, status=400)

    data = {
        'message': 'Successfully Created.',
        'result': {
            'id': product.id,
            'name': product.name,
            'price': product.price,
        }
    }
    return JsonResponse(data)


def get_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        data = {
            'error': 'Not Found product {0}'.format(product_id)
        }
        return JsonResponse(data, status=404)

    data = {
        'result': {
            'id': product.id,
            'name': product.name,
            'price': product.price,
        }
    }
    return JsonResponse(data)


def update_product(request, product_id):
    if request.headers.get('Content-Type') != 'application/json':
        data = {
            'error': 'Bad Request: Content-Type must be application/json.'
        }
        return JsonResponse(data, status=400)

    body = json.loads(request.body)
    name = body.get('name')
    price = body.get('price')
    if name is None or price is None:
        data = {
            'error': 'Bad Request: The key "name" and "price" are required.'
        }
        return JsonResponse(data, status=400)

    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        data = {
            'error': 'Not Found product {0}'.format(product_id)
        }
        return JsonResponse(data, status=404)

    try:
        product.name = name
        product.price = price
        product.full_clean()
        product.save()
    except ValidationError:
        data = {
            'error': 'Bad Request: Bad data.'
        }
        return JsonResponse(data, status=400)

    data = {
        'message': 'Successfully Updated.',
        'result': {
            'id': product.id,
            'name': product.name,
            'price': product.price,
        }
    }
    return JsonResponse(data)


def delete_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        data = {
            'error': 'Not Found product {0}'.format(product_id)
        }
        return JsonResponse(data, status=404)

    deleted_product = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
    }
    product.delete()
    data = {
        'message': 'Successfully Deleted.',
        'result': deleted_product
    }
    return JsonResponse(data)
