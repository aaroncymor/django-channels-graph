"""
ASGI config for channels_tutorial project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from graph.routing import ws_urlpatterns as graph_urls
from jokes.routing import ws_urlpatterns as jokes_urls


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels_tutorial.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(graph_urls + jokes_urls))
}) 
