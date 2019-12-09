"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
You can read more about URLs in https://docs.djangoproject.com/en/3.0/topics/http/urls/ dispatcher.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()
