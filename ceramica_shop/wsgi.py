"""
Fichier WSGI pour le projet ceramica_shop.

Il expose l'appel WSGI en tant que variable de niveau module nommée ``application``.

Pour plus d'informations sur ce fichier, consultez
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ceramica_shop.settings')
application = get_wsgi_application()
