from django.http.response import JsonResponse


def get_products(request):
    products =  {
        'result': [
            {
                'id': 1,
                'name': 'book',
                'price': 600
            },
            {
                'id': 2,
                'name': 'fisj',
                'price': 200
            },
        ]
    }
    return JsonResponse(products)
