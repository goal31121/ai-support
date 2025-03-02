# Use official Python image
#Uses the official Python 3.13 slim image as the base.
#slim means it’s lightweight, so the container is smaller and faster.
FROM python:3.13-slim

# Set environment variables
#PYTHONDONTWRITEBYTECODE=1 → Python won’t create .pyc files.
#PYTHONUNBUFFERED=1 → Python prints logs immediately (useful for Docker logs).
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
#PYTHONDONTWRITEBYTECODE=1 → Python won’t create .pyc files.
#PYTHONUNBUFFERED=1 → Python prints logs immediately (useful for Docker logs).
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Copy and set entrypoint
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expose port
#Exposes port 8000 so you can access Django from outside the container (localhost:8000).
EXPOSE 8000

# Use entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

#This Dockerfile builds a Python/Django environment, installs dependencies, 
#copies your project, and starts it using an entrypoint.sh script. 
#The exposed port allows you to run the Django server inside Docker and access it from your browser.