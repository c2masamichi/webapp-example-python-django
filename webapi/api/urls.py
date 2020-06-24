from django.urls import path

from . import views

app_name = 'api_v1'
urlpatterns = [
    path('products', views.get_products, name='list'),
]
