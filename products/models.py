# Modèle de produit

from django.db import models

# Cher collègue,

# Voici notre modèle de produit qui définit la structure de données
# pour les produits que nous stockons dans notre base de données.
# Les modèles sont essentiels dans Django car ils définissent les
# tables de notre base de données et les relations entre elles.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    image_url = models.URLField()

    # Méthode spéciale __str__() pour représenter le produit par son nom
    def __str__(self):
        return self.name

    class Meta:
        app_label = 'products'

# Dans ce modèle, nous définissons plusieurs champs pour stocker les
# informations relatives à un produit, telles que le nom, la description,
# le prix, la catégorie et l'URL de l'image.

# La méthode spéciale __str__() est utilisée pour afficher une
# représentation conviviale du produit lorsque nous l'utilisons dans 
# des opérations d'affichage ou de journalisation.

# Le champ 'app_label' est utilisé pour spécifier l'étiquette d'application
# associée à ce modèle. Cela aide à organiser les modèles si vous avez
# plusieurs applications dans votre projet Django.

# N'hésitez pas à explorer et à utiliser ce modèle pour représenter
# nos produits dans la base de données.

# Cordialement,
# Christian Pazmany, Votre collègue bien aimé !!!
