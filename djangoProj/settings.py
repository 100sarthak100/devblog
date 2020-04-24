"""
Django settings for djangoProj project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '0v4%a84s7b%9iupsri-eg=l0$wxe_)gyifcns%1jg=5wixm+o9'
SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')

ALLOWED_HOSTS = ['devblogapp.herokuapp.com','www.mydevblog.me','mydevblog.me']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'robots',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'tinymce',
    'taggit',
    'crispy_forms',
    'channels',
    'chat',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
ROOT_URLCONF = 'djangoProj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'djangoProj.wsgi.application'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
import dj_database_url
DATABASES['default'] = dj_database_url.config(default=DATABASE_URL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR,  'templates'),
#     # Add to this list all the locations containing your static files 
# )

TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 'auto',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': 'formatselect | bold italic underline | alignleft aligncenter alignright alignjustify '
               '| bullist numlist | outdent indent | table | link image | codesample | preview code',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'inline': False,
    'statusbar': True,
    'content_css': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css',
    }

TINYMCE_JS_URL = '//cdn.tinymce.com/4/tinymce.min.js'

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

LOGIN_REDIRECT_URL = 'blogHome'
LOGIN_URL = 'login'

# django_heroku.settings(locals())

# Channels
ASGI_APPLICATION = "djangoProj.routing.application"
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             #"hosts": [("localhost", 6379)],
#             "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
#         },
#     },
# }

CHANNEL_LAYERS = {
    "default": {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
        #"ROUTING": "chat.routing.channel_routing",
    },
}

IS_CI = os.environ.get('IS_CI', False)
if not IS_CI:
    django_heroku.settings(locals())