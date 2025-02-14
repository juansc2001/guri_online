"""
WSGI config for setup project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import os
import sys
from django.core.wsgi import get_wsgi_application

#acrescentei isso
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(BASE_DIR)
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.development'
#acrescentei isso 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

application = get_wsgi_application()
