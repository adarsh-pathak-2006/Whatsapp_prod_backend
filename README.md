# WhatsApp Backend API

This is the backend API for a WhatsApp clone, built with Django and Django REST Framework.

## Features
- **User Authentication**: Secure token-based authentication using JWT.
- **One-on-One Chat**: Private real-time messaging between users.
- **Group Chat**: Create groups, add members, assign admins, and chat in groups.
- **Contact Management**: Add and manage user profiles in a contact list.
- **Production Ready**: Configured with `gunicorn`, `whitenoise`, and `django-environ` for easy deployment to platforms like Render, Heroku, or AWS.

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/adarsh-pathak-2006/Whatsapp_prod_backend.git
cd Whatsapp_prod_backend/whatsapp
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Copy the example environment file and configure it:
```bash
cp .env.example .env
```
Ensure `DEBUG=True` for local development.

### 5. Database Migrations
Run the initial database migrations:
```bash
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

## Production Deployment

This project is configured for deployment using standard 12-factor app methodologies.

### Environment Variables for Production
Set the following environment variables on your hosting platform:
- `DEBUG=False`
- `SECRET_KEY=your_secure_secret_key`
- `ALLOWED_HOSTS=yourdomain.com,yourapi.render.com`
- `CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com`
- `DATABASE_URL=postgres://user:password@hostname:5432/dbname` (For PostgreSQL)

### WSGI Server
The project is configured to use Gunicorn in production:
```bash
gunicorn whatsapp.wsgi:application
```

### Static Files
Static files are automatically handled and served by WhiteNoise.

## API Documentation

The API includes endpoints for:
- `/register/`: User registration.
- `/token/`: Obtain JWT tokens.
- `/api/chat/`: Manage private chats and messages.
- `/api/group/`: Manage group creation, members, and group chats.
- `/api/contact/`: Manage contacts and profiles.
