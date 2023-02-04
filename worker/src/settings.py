"""
Django settings for credit_policy project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*5y#8fmuo+45^(+)np(rs4(3z3zexrhjmsucr)obybr@d3o3@m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
	'django.contrib.contenttypes',
	'django.contrib.staticfiles',
	'applications.crawler'
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = None


DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'HOST': os.environ.get('MY_DB_HOST', 'localhost'),
		'PORT': os.environ.get('MY_DB_PORT', '6932'),
		'NAME': os.environ.get('MY_DB_NAME', 'crawler_data', ),
		'USER': os.environ.get('MY_DB_USER', 'postgres'),
		'PASSWORD': os.environ.get('MY_DB_PASSWORD', 'postgres')
	}
}


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

QUEUE_CONN_PARAMS = {
	"host": os.environ.get("REDIS_HOST", "localhost"),
	"port": os.environ.get("REDIS_PORT", 6381)
}
