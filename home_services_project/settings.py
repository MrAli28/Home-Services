import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h3m4k5l6m7n8o9p0q1r2s3t4u5v6w7x8y9z0a1b2c3d4e5f6g7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# CSRF Settings
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://127.0.0.1:52464']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'services',  # Our main app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'home_services_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'home_services_project.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication settings
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'  

# Custom authentication backends
AUTHENTICATION_BACKENDS = [
    'services.backends.EmailOrUsernameModelBackend',  # Our custom backend
    'django.contrib.auth.backends.ModelBackend',  # Default backend
]

# Email Configuration - Using Gmail SMTP for reliable delivery
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'huss133236@gmail.com'  # Your Gmail address as sender
EMAIL_HOST_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD', '')  # App password

# Brevo specific settings
BREVO_API_KEY = os.environ.get('BREVO_API_KEY', '')  # Get from environment variable

# WhatsApp Business Platform settings
WHATSAPP_BUSINESS_TOKEN = os.environ.get('WHATSAPP_BUSINESS_TOKEN', '')
WHATSAPP_PHONE_NUMBER_ID = os.environ.get('WHATSAPP_PHONE_NUMBER_ID', '')

# Admin notification settings
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'huss133236@gmail.com')
ADMIN_WHATSAPP = os.environ.get('ADMIN_WHATSAPP', '+923061642273')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'noreply@homefix.com')  # Default sender address

# CSRF settings for browser preview
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:61866', 'http://localhost:8000', 'http://127.0.0.1:8000']
CSRF_COOKIE_DOMAIN = None
CSRF_COOKIE_SECURE = False  # Set to True in production
CSRF_COOKIE_HTTPONLY = False  # Allow JavaScript to access the cookie
CSRF_USE_SESSIONS = True  # Store CSRF token in session instead of cookie
CSRF_COOKIE_SAMESITE = None  # 'Lax', 'Strict', or None

# For Django 4.0+, also need to set this
ALLOWED_HOSTS = ['*']  # Allow all hosts in development

# Session settings
SESSION_COOKIE_SECURE = False  # Set to True in production
SESSION_COOKIE_HTTPONLY = True
