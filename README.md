### AI-Powered Customer Support Interface (Dockerized)
---
This repository contains the Dockerized version of the AI-powered customer support interface. It allows running the Django application inside a container for easier deployment and environment management.

---
### Features 
1. Run the Django app in a Docker container.
2. Preconfigured dependencies via requirements.txt.
3. Easy setup without installing Python or other libraries locally.
4. Supports existing database migrations and superuser creation.
---
### Prerequisites
Docker installed on your system.

---
### Setup Instruction
1. Clone the Repository
```bash
git clone https://github.com/aahanabobade/ai_support_app_docker.git
cd ai_support_app_docker
```
2. Build the Docker Image
```bash
docker build -t ai_support_app .
```
3. Create a Docker Volume for Database Persistence
```bash
docker volume create ai_support_db
```
This ensures that your SQLite database is stored outside the container, so your data is not lost when the container stops.

4. Run the docker container with volume

```bash
docker run -p 8000:8000 -v ai_support_db:/app/db.sqlite3 ai_support_app
```
-p 8000:8000 maps the container port to your local machine.
-v ai_support_db:/app/db.sqlite3 mounts the database file to persist data.

5. Apply Migrations( first time only)
Open a terminal into the running container:
```bash
docker exec -it <container_id> bash
```

6. Inside the container, run:
```bash
python manage.py migrate
```

7. Access the App
Visit in your browser: http://127.0.0.1:8000

8. Stop the Container
```bash
docker stop <container_id>
```
Your data remains safe because of the Docker volume.


### Assumptions

1. The app uses SQLite database inside the container by default.
2. The AI response feature requires a valid API key (e.g., Gemini API or OpenAI).
3. Users (admin or customers) can be created through the app interface.

### Limitations

1. This setup is meant for development/testing purposes.
2. For production, use a production-ready WSGI server (like Gunicorn) and a more robust database (like PostgreSQL).
3. The AI API key should be set in environment variables or a .env file inside the container for security.

### Tech Stack
1. Python 3.13, Django 5.2
2. Docker for containerization
3. SQLite database
4. Gemini API for AI integration for auto-generated responses

### Note:

1. Single Machine Testing: The system is tested locally; production deployment may require Docker, a web server, and proper environment variable management.
2. AI Reliability: AI responses might occasionally require manual correction.
3. No Multi-language Support: Currently supports only English.
4. Basic UI/UX: Focus is on functionality rather than advanced design.
5. Admin Panel Role Check: Admin cannot act as customer, but the interface is basic and could be enhanced with detailed role validation messages.


### Contact/Support
This project is maintained by Aahana Bobade. For any issues or questions regarding setup or usage, please contact via GitHub or email(aahanabobade@gmail.com).
