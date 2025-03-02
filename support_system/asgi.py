"""
ASGI config for support_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""
"""
2. ASGI (Asynchronous Server Gateway Interface)
	•	ASGI is for asynchronous Python web apps.
	•	Handles real-time features like WebSockets, chat apps, notifications.
	•	It’s like WSGI but supports async operations (multiple requests at the same time without blocking).

Example use case:
	•	A live chat support feature where messages appear instantly without refreshing the page.
	•	ASGI allows your server to handle that alongside normal HTTP requests.
 """
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'support_system.settings')

application = get_asgi_application()
