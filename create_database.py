import mysql.connector

# Paramètres de connexion à la base de données
db_params = {
    'host': 'localhost',
    'user': 'root',
    'password': 'fms2023',
}

# Chers collègues,
# Le bloc suivant tente de se connecter à la base de données MySQL en utilisant les paramètres spécifiés.
try:
    conn = mysql.connector.connect(**db_params)
except mysql.connector.Error as err:
    # Si l'accès à la base de données est refusé, affichons une erreur appropriée.
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erreur : Accès refusé à la base de données")
    # Si la base de données n'existe pas, nous allons la créer.
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print("La base de données n'existe pas, nous allons la créer...")
        conn = mysql.connector.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE ceramica_shop_db")
        print("Base de données créée avec succès !")
        cursor.close()
    else:
        print(err)

# Chers collègues,
# Maintenant que nous avons établi la connexion à la base de données, nous allons exécuter les migrations Django.
if conn.is_connected():
    conn.close()
    print("Exécution des migrations Django...")
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceramica_shop.settings')
    from django.core.management import execute_from_command_line
    # Nous exécutons d'abord la commande 'makemigrations' pour créer les fichiers de migration.
    execute_from_command_line(['manage.py', 'makemigrations'])
    # Ensuite, nous exécutons la commande 'migrate' pour appliquer les migrations et créer les tables dans la base de données.
    execute_from_command_line(['manage.py', 'migrate'])
    print("Migrations exécutées avec succès !")

