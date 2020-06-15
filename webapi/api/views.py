from django.http import HttpResponse


def get_products(request):
    return HttpResponse(
        {
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
    )
