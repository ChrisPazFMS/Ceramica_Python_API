"""
URL configuration for ceramica_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from products.views import ProductList

urlpatterns = [
    # Chemin vers la liste des produits de l'API
    path('api/products/', ProductList.as_view(), name='product-list'),
    
    # Chemin vers l'interface d'administration Django
    path('admin/', admin.site.urls),
    
    # Inclure les URLs de l'application products
    path('', include('products.urls')),
]
