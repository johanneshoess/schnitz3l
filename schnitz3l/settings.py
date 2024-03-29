"""
Django settings for schnitz3l project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print('BASE_DIR', BASE_DIR.parent)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    print('ERROR - secret key not available!')
else:
    print("Your Django Secret Key was added")

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv("DEBUG") == 'True':
    DEBUG = True
else:
    DEBUG = False

if DEBUG:
    print('###########   in DEBUG mode   ##########')
    p = """
         .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
        | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
        | |  ________    | || |  _________   | || |   ______     | || | _____  _____ | || |    ______    | |
        | | |_   ___ `.  | || | |_   ___  |  | || |  |_   _ \    | || ||_   _||_   _|| || |  .' ___  |   | |
        | |   | |   `. \ | || |   | |_  \_|  | || |    | |_) |   | || |  | |    | |  | || | / .'   \_|   | |
        | |   | |    | | | || |   |  _|  _   | || |    |  __'.   | || |  | '    ' |  | || | | |    ____  | |
        | |  _| |___.' / | || |  _| |___/ |  | || |   _| |__) |  | || |   \ `--' /   | || | \ `.___]  _| | |
        | | |________.'  | || | |_________|  | || |  |_______/   | || |    `.__.'    | || |  `._____.'   | |
        | |              | || |              | || |              | || |              | || |              | |
        | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
         '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
    """
    print(p)
    CSRF_TRUSTED_ORIGINS = [
        'https://nebukat.uber.space',
        'http://127.0.0.1:8000',
        'http://localhost:8000',
        'https://n3bu.lol'
    ]
    ALLOWED_HOSTS = [
        'nebukat.uber.space',
        '127.0.0.1',
        'localhost',
        'n3bu.lol'
    ]
    CORS_ORIGIN_WHITELIST = [
        'https://nebukat.uber.space',
        '127.0.0.1:8000',
        'localhost:8000',
        'https://n3bu.lol'
    ]
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
else:
    print("started in Production Mode")
    CSRF_TRUSTED_ORIGINS = [
        'https://nebukat.uber.space',
        'https://www.n3bu.lol'
    ]
    ALLOWED_HOSTS = [
        'nebukat.uber.space',
        'www.n3bu.lol',
        'n3bu.lol'
    ]
    CORS_ORIGIN_WHITELIST = [
        'https://nebukat.uber.space',
        'https://www.n3bu.lol'
    ]
    STATIC_ROOT = os.getenv('STATIC_ROOT')


# Application definition

INSTALLED_APPS = [
    'jagd.apps.JagdConfig',
    'n3bu.apps.N3buConfig',
    'vtanz.apps.VtanzConfig',
    'r3cord.apps.R3CordConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap4',
    'pagedown.apps.PagedownConfig'
]

# Crispy Forms Template
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'schnitz3l.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'schnitz3l.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASE = os.getenv("DATABASE")

if DATABASE == 'Postgres':
    name = os.getenv("DATABASE_NAME")
    username = os.getenv("DATABASE_USERNAME")
    password = os.getenv("DATABASE_PASSWORD")
    host = os.getenv("DATABASE_HOST")
    port = os.getenv("DATABASE_PORT")

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': name,
            'USER': username,
            'PASSWORD': password,
            'HOST': host,
            'PORT': port,
        }
    }
elif DATABASE == 'SQLite':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif DATABASE == 'mariaDB':
    name = os.getenv("DATABASE_NAME")
    username = os.getenv("DATABASE_USERNAME")
    password = os.getenv("DATABASE_PASSWORD")
    host = os.getenv("DATABASE_HOST")
    port = os.getenv("DATABASE_PORT")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            'NAME': name,
            'USER': username,
            'PASSWORD': password,
            'HOST': host,
            'PORT': port,
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'CET'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# location for uploading side view photos, images uploaded in admin gui also go to upload/media
if not DEBUG:
    BASE_DIR = BASE_DIR.parent / 'html'

STATIC_DIR = BASE_DIR / 'static'
MEDIA_DIR = BASE_DIR / 'media'
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'
