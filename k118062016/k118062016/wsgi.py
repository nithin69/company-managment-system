"""
WSGI config for k118062016 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import os,sys
sys.path.append('/home/thiru/k1groups/k118062016')


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "k118062016.settings")

application = get_wsgi_application()
