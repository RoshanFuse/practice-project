"""
ASGI config for crudproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

#  for websoket

from channels.routing import ProtocolTypeRouter,URLRouter
import enroll.websocket.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudproject.settings')

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': URLRouter(
            enroll.websocket.routing.websocket_urlpatterns
        )
    }
)
