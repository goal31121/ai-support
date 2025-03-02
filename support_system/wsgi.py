"""
WSGI config for support_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
"""1. WSGI (Web Server Gateway Interface)
	•	WSGI is for synchronous Python web applications.
	•	It’s the standard interface between web servers (like Gunicorn, Apache) and Python web apps (like Django, Flask).
	•	Think of it as a bridge: Web server → Python app.
	•	Django uses WSGI by default for normal development or production servers.

Example use case:
	•	Your Django app receives a user request (like opening /tickets/).
	•	WSGI passes that request from the web server to Django.
	•	Django processes it and sends the response back through WSGI to the web server → browser."""
 
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'support_system.settings')

application = get_wsgi_application()
