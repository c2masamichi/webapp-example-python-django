from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator
from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=20, unique=True,
        validators=[MinLengthValidator(3), RegexValidator(r'^[0-9a-zA-Z ]*$')]
    )
    price = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(1000000000)]
    )
