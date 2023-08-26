#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Exécute les tâches administratives de Django."""
    # Configure les paramètres d'environnement pour utiliser les réglages Django.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceramica_shop.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible d'importer Django. Êtes-vous sûr qu'il est installé et "
            "disponible dans votre variable d'environnement PYTHONPATH ? Avez-vous "
            "oublié d'activer un environnement virtuel ?"
        ) from exc
    # Exécute la commande Django spécifiée en ligne de commande.
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
