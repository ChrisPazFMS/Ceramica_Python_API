# Ceramica_Python_API

Guide de démarrage et de gestion pour l'API ceramica_shop

Ce guide vous fournira les étapes nécessaires pour initialiser, gérer et développer l'API ceramica_shop.

Tout d'abord mettez-vous à la racine du programme, avec la commande ls ou dir vous devez voir afficher (manage.py\*).

XXXX - Tout d'abord vous créez votre base de données en ligne de commande directement, parce qu'a priori Django ne le fait pas - XXXX
mysql -u root -p
CREATE DATABASE ceramica_shop_db;
GRANT ALL PRIVILEGES ON ceramica_shop_db.\* TO 'root'@'localhost';
FLUSH PRIVILEGES;
python create_database.py //Voilà votre base de données a été créé

// Démarrer votre serveur python API
python manage.py runserver

Make the most of it!!!!!!
Maintenant si vous avez tout réussi correctement, vous devez pouvoir utiliser les requêtes !

Chers collègues, je vous transmets les routes pour réaliser les CRUD, bien à vous !

POST : http://localhost:8000/api/products/create-product/
GET : http://127.0.0.1:8000/api/products/
DELETE : http://localhost:8000/api/products/1/delete/
PUT : http://localhost:8000/api/products/1/update/

Vous disposez aussi des modèles JSON pour les utiliser dans les requêtes dans le fichier.
creation_product.json

I. Création de la base de données :

1.  Créer les migrations : python manage.py makemigrations
2.  Appliquer les migrations : python manage.py migrate
3.  Créer un superutilisateur : python manage.py createsuperuser

II. Mise en route du serveur pour l'API :

1.  Démarrer le serveur : python manage.py runserver
2.  Accéder à l'API : http://127.0.0.1:8000/
3.  Vérifier l'API en accédant à la page d'accueil de Django.

III. Procédure de modification des tables :

1.  Modifier le modèle dans le fichier models.py.
2.  Créer une migration pour les modifications : python manage.py makemigrations
3.  Appliquer les modifications : python manage.py migrate

IV. Procédure de développement :

/\***\* Faites attention cher collègue,
Dans le fichier [views.py] nous ne gérons pas la vue, mais uniquement des fichiers de JSON \*\***/

1.  Créer de nouvelles vues : Définir vos vues dans le fichier views.py.
2.  Créer des sérialiseurs : Définir vos sérialiseurs dans le fichier serializers.py.
3.  Configurer les URLs : Définir vos URLs dans le fichier urls.py.
4.  Effectuer des tests : Écrire et exécuter des tests pour s'assurer que l'API fonctionne correctement.

V. Gestion de Git :

/\***\* Et pour finir je vous rappelle les commandes Git, pour créer votre repository, et faire évoluer votre nouvelle API python. \*\***/

1.  Initialiser Git : git init
2.  Créer un nouveau dépôt : git remote add origin <URL_du_dépôt>
3.  Ajouter et valider les changements : git add . && git commit -m "Message de commit"
4.  Pousser les changements vers GitHub : git push origin main

# Cordialement,

# Christian Pazmany, Votre collègue bien aimé !!!

Chers collègues, chers futurs Pythoniens,
Je suis heureux d'avoir finaliser un projet python, pour créer une API, avec la bibliothèque très connue de Django, elle permet de réaliser une api back-end, je crois bien que c'est une des plus connues et les plus utilisés, vu qu'elle fonctionne à merveille !

Je vous transmets le lien que GitHub pour récupérer le fichier et le tester, il y a tous les commentaires qui vont bien pour comprendre le code, il y a la possibilité de réaliser les CRUD.
Toutes les instructions sont dans le fichier Readme.

Je me suis fait plaisir de vous transmettre cette petite API python.
Pour les curieux et pour ceux qui le désirent,
Parce que je vous apprécie tous beaucoup !
De la part de votre collègue bien aimé.

Cordialement, christian.
