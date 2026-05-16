Nice — adding rate limiting is a solid touch for auth endpoints 🔥

Since this is something you’ll likely want to reuse on GitHub, here’s a clean README structure you can copy and paste directly.

````md
# Django Google OAuth Authentication API

A production-style Google OAuth authentication system built with Django REST Framework and JWT authentication.

This project provides a secure backend authentication service using Google Sign-In, token verification, JWT authentication, rate limiting, and user creation/login handling.

## Features

- Google OAuth Authentication
- Google ID Token Verification
- JWT Authentication using Simple JWT
- Automatic User Creation/Login
- Secure Email Verification
- Token Validation
- Rate Limiting Protection
- Clean Service Layer Architecture
- Serializer-based Request Validation
- REST API Ready
- Backend-focused Authentication Flow

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- Google OAuth2
- Django Rate Limit
- SQLite (can be switched to PostgreSQL/MySQL)

---

## Project Structure

```text
app/
│
├── google_auth/
│   ├── services.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── throttles.py
│
├── settings.py
│
└── manage.py
````

---

## Authentication Flow

```text
User clicks Google Login
          ↓
Google returns ID Token
          ↓
Frontend sends token to Django API
          ↓
Backend verifies token with Google
          ↓
User created or fetched
          ↓
JWT Access & Refresh Tokens generated
          ↓
Authenticated user returned
```

---

## API Endpoint

### Google Login

**POST**

```http
/api/google-login/
```

### Request Body

```json
{
  "id_token": "google_id_token_here"
}
```

### Success Response

```json
{
  "status": true,
  "message": "Google login successful",
  "user": {
    "email": "user@gmail.com",
    "user_name": "user@gmail.com",
    "first_name": "John",
    "last_name": "Doe"
  },
  "tokens": {
    "access": "jwt_access_token",
    "refresh": "jwt_refresh_token"
  }
}
```

### Error Response

```json
{
  "status": false,
  "message": "Invalid or expired Google token"
}
```

---

## Google OAuth Setup

### 1. Create Google Cloud Project

Go to Google Cloud Console and create a project.

### 2. Configure OAuth Consent Screen

* Choose **External**
* Add application details
* Add test users (if in testing mode)

### 3. Create OAuth Client ID

Navigate to:

```text
APIs & Services → Credentials
```

Create:

```text
OAuth Client ID → Web Application
```

Add Authorized JavaScript Origins:

```text
http://127.0.0.1:5500
http://localhost:5500
```

(Adjust ports depending on your frontend/test environment)

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_CLIENT_ID=your_google_client_id
REDIS_URL=your_redis_url
DEBUG=True
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/yourusername/project-name.git
```

Move into project:

```bash
cd project-name
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start server:

```bash
python manage.py runserver
```

---

## Security Features

### Google Token Verification

The backend securely verifies:

* Token signature
* Token expiration
* Token issuer
* Client ID audience
* Verified Google email

### Rate Limiting

Authentication endpoints are rate-limited to reduce abuse and brute-force attacks.

### JWT Authentication

Authenticated users receive:

* Access Token
* Refresh Token

---

## Future Improvements

* Store Google `sub` as unique identity
* HTTP-only cookie authentication
* Token refresh rotation
* Multi-provider OAuth (GitHub, Facebook)
* User profile endpoint
* Role-based permissions

---

## Author

Built by Hussein Lawal.

````

Before pushing:

1. Add a good repo name like:

```text
django-google-oauth-auth-api
````

2. Add screenshots or Postman examples later.

3. Make sure `.env` is in `.gitignore`:

```gitignore
.env
venv/
__pycache__/
db.sqlite3
```

This README will already look professional for GitHub and portfolio.
