from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('collections/', views.collections, name='collections'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
]
