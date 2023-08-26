
# On utilise pas cette importation, elle sert juste à créer des vues HTML depuis le back end, tout comme le faisait Thymeleaf.
# from django.shortcuts import render

# Importations
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView

# Vue pour lister tous les produits
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Cher collègue, cette vue permet de lister tous les produits disponibles.

# Vue pour créer un nouveau produit
@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product = Product.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            category=data['category'],
            image_url=data['image_url']
        )
        response_data = {
            "message": "Product created successfully",
            "product": {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "category": product.category,
                "image_url": product.image_url
            }
        }
        return JsonResponse(response_data, status=201)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)
    # Cher collègue, cette vue permet de créer un nouveau produit en utilisant les données fournies.

# Vue pour supprimer un produit
class ProductDeleteView(APIView):
    def delete(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    # Cher collègue, cette vue permet de supprimer un produit existant à l'aide de son identifiant.

# Vue pour récupérer et mettre à jour un produit
class ProductUpdateView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Cher collègue, cette vue permet de récupérer et de mettre à jour les informations d'un produit.
