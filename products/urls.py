# Configuration des URLs Django

from django.urls import path
from .views import ProductList, ProductUpdateView, create_product, ProductDeleteView

urlpatterns = [
    # Liste de tous les produits
    path('api/products/', ProductList.as_view(), name='product-list'),

    # Création d'un nouveau produit
    path('api/products/create-product/', create_product, name='create-product'),

    # Suppression d'un produit par ID
    path('api/products/<int:product_id>/delete/',
         ProductDeleteView.as_view(), name='delete-product'),

    # Mise à jour d'un produit par ID
    path('api/products/<int:pk>/update/',
         ProductUpdateView.as_view(), name='update-product'),
]
