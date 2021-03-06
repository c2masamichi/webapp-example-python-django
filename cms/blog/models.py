from django.db import models
from django.utils import timezone


class Entry(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000)
    created = models.DateTimeField(default=timezone.now, editable=False)