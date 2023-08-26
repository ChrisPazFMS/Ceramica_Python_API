"""
ASGI config for ceramica_shop project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Configuration des paramètres du projet
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceramica_shop.settings') 

# Obtention de l'application ASGI Django
application = get_asgi_application()
