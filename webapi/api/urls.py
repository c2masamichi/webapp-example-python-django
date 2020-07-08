from django.urls import path

from . import views

app_name = 'api_v1'
urlpatterns = [
    path('products', views.list_or_create_product),
    path('products/<int:product_id>', views.get_or_update_or_delete_product),
]
