# Cher collègue,
# La classe ProductsConfig est utilisée pour configurer l'application 'products' dans Django.
# Elle définit le type de champ auto-incrémenté à utiliser pour les clés primaires de la base de données.
# Dans notre cas, nous utilisons 'django.db.models.BigAutoField' pour les clés primaires.
# Cela est utile lorsque nous effectuons des migrations de base de données.
from django.apps import AppConfig

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
