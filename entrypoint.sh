#!/bin/bash
# Apply database migrations
python manage.py migrate

# Start Django server
python manage.py runserver 0.0.0.0:8000


#0.0.0.0 → Makes it accessible from outside the container (so you can access it via localhost:8000).
#8000 → Matches the port you exposed in the Dockerfile.