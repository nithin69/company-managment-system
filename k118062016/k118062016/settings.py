"""
Django settings for k118062016 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os
import socket
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(m%e!hrq*%wnk$#8)$ibgd5_fttfkdd8$)y9is3rn0qs3rfr@k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'dal',
    'dal_select2',
    'dal_queryset_sequence',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myproject',
    'registration',
    'rest_framework',
    'smart_selects',
    'import_export',
    'tracking',
    #'adminrestrict',
    'jsignature',
    'notifications',
    #'django_admin_generator',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'adminrestrict.middleware.AdminPagesRestrictMiddleware',
    #'tracking.middleware.VisitorTrackingMiddleware',
)

ROOT_URLCONF = 'k118062016.urls'

WSGI_APPLICATION = 'k118062016.wsgi.application'


NOTIFICATIONS_USE_JSONFIELD=True

NOTIFICATIONS_SOFT_DELETE=True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if socket.gethostname() == 'Sam-PC':
    DEBUG = TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = ['*']
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'kcitsplc_ssms',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',
	'OPTIONS': {
         "init_command": "SET foreign_key_checks = 0;",
    },                      # Set to empty string for default.
    }
}
elif socket.gethostname() == 'ubuntu':
    DEBUG = TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = ["k1groups.in:8000", "www.k1groups.in:8000"]
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'kcitsplc_ssms',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',
	'OPTIONS': {
         "init_command": "SET foreign_key_checks = 0;",
    },                      # Set to empty string for default.
    }
}

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'kcitsplc_ssms',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',
	'OPTIONS': {
         "init_command": "SET foreign_key_checks = 0;",
    },                      # Set to empty string for default.
    }
}'''


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/



LANGUAGE_CODE = 'en-us'

TIME_ZONE =  'Asia/Kolkata'
MEDIA_URL = '/media/'
USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_ACTIVATION_DAYS = 7 
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')


#AUTH_USER_MODEL = 'k1emp.Employee'


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
    		"django.core.context_processors.debug",
    		"django.core.context_processors.i18n",
   		"django.core.context_processors.media",
    		'django.template.context_processors.request',
    		'django.core.context_processors.request',
    		"django.core.context_processors.static",
    		"django.core.context_processors.tz",
    		"django.contrib.messages.context_processors.messages",
            ],
        },
    },
]



#MATERIAL_ADMIN_SITE = 'mymodule.admin.admin_site'

STATIC_PATH=os.path.join(BASE_DIR, '../static')
STATIC_ROOT='/'

STATIC_URL = '/static/' # You may find this is already defined as su
STATICFILES_DIRS = (
    STATIC_PATH,
)

MEDIA_URL = '/media/'
STATIC_URL = '/static/' # You may find this is already defined as such.

MEDIA_ROOT = os.path.join(BASE_DIR, '../media')

CSRF_COOKIE_DOMAIN = None



