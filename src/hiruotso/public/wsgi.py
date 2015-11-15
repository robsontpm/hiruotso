"""
WSGI config for hiruotso project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/

Settings are separated from wsgi.py as wsgi.py must be publicly available on the
production server (e.g. apache), which is bad for settings :)
"""

import os

from django.core.wsgi import get_wsgi_application

# use production setting on wsgi server
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.production")

application = get_wsgi_application()
