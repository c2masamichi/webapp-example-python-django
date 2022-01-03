from django.core.exceptions import ValidationError
import pytest

from api.models import Product


@pytest.mark.django_db
@pytest.mark.parametrize(
    ('name', 'price'),
    (
        ('aa', 1000),
        ('a' * 21, 1000),
        ('house', 1000000001),
        ('minus', -1),
        ('A 01 %', 100),
    ),
)
def test_create_validate(name, price):
    with pytest.raises(ValidationError):
        product = Product(name=name, price=price)
        product.full_clean()


@pytest.mark.django_db
@pytest.mark.parametrize(
    ('name', 'price'),
    (
        ('aa', 1000),
        ('a' * 21, 1000),
        ('house', 1000000001),
        ('minus', -1),
        ('A 01 %', 100),
    ),
)
def test_update_validate(name, price):
    product_id = 2
    product = Product.objects.get(pk=product_id)
    with pytest.raises(ValidationError):
        product.name = name
        product.price = price
        product.full_clean()
