from .base import *

DEBUG = False

SECRET_KEY = 'django-insecure-!av7c**ni9pvtazs)e4kkv&(3gm7mk54=gu2a=pcmquo8g=l&+'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'library',
        'USER': 'denis',
        'PASSWORD': 'qwerty',
        'HOST': 'db',
        'PORT': '5432',
    }
}
