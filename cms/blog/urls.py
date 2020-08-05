from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('entry/<int:entry_id>', views.detail, name='detail'),
]