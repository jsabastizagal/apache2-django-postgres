# -*- coding: utf-8 -*-
"""
Django settings for vetadminproject project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from vetadminproject.paths import PROJECT_DIR
from vetadminproject.paths import PROJECT_NAME
from vetadminproject.paths import VAR_ROOT

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0730$g285s_s57j$*d_n$s6jdpx-w^aq#5!9as(2n@x+a3_1-3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['45.56.93.71','localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'medicalConsultation',
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

ROOT_URLCONF = 'vetadminproject.urls'

TEMPLATE_BASE_DIR = os.path.join(PROJECT_DIR, PROJECT_NAME, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_BASE_DIR,
            os.path.join(PROJECT_DIR, 'medicalConsultation', 'templates'),
            ],
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

WSGI_APPLICATION = 'vetadminproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'vetadmin',
#         'USER': 'vetadminuser',
#         'PASSWORD': 'visual.02',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

def env(name):
    return os.environ.get(name, None)



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/
TIME_ZONE = 'America/Santiago'
LANGUAGE_CODE = 'es-CL'
USE_I18N = True
USE_L10N = True
USE_TZ = True
SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
#     '/var/www/vetadminweb/vetadminproject/static',
# ]
#
# STATIC_ROOT = '/var/www/vetadminweb/vetadminproject/static'


STATIC_URL = '/static/'




if env('ENV_SETTING') == 'dev':
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
        os.path.join(PROJECT_DIR, PROJECT_NAME),
    )
    STATIC_ROOT = '/var/www/vetadminweb/vetadminproject/static'

if env('ENV_SETTING') == 'prod':
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
        '/var/www/vetadminweb/vetadminproject/static',
    ]
