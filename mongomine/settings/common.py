from os.path import abspath, basename, dirname, join, normpath
from sys import path
from configurations import Configuration
from django.core.urlresolvers import reverse_lazy
from .logger_settings import LoggerSettingsMixin
import os


class Settings(LoggerSettingsMixin, Configuration):
    DJANGO_ROOT = dirname(dirname(abspath(__file__)))

    SITE_ROOT = dirname(DJANGO_ROOT)

    SITE_NAME = basename(DJANGO_ROOT)

    path.append(DJANGO_ROOT)

    DEBUG = True

    ENV = 'development'

    ADMINS = ()

    TIME_ZONE = 'Asia/Kolkata'

    USE_TZ = False

    LANGUAGE_CODE = 'en-us'

    USE_I18N = True

    USE_L10N = True

    MEDIA_ROOT_DIR = 'media'
    MEDIA_ROOT = normpath(join(DJANGO_ROOT, MEDIA_ROOT_DIR))
    MEDIA_URL = '/media/'

    STATIC_ROOT_DIR = 'static'
    STATIC_ROOT = normpath(join(DJANGO_ROOT, STATIC_ROOT_DIR))
    STATIC_URL = '/static/'

    SITE_ID = 1

    STATICFILES_DIRS = (
	normpath(join(DJANGO_ROOT, 'ver_static')),
    )

    # To Serve The Static Pages
    EXPOSE_STATIC_URLS = True

    # See:
    # https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'compressor.finders.CompressorFinder',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
    )

    SECRET_KEY = '5ai%65$g_0*(0l$d@g5i8pohpc&d3id6z@doj4ddyl9v0#zhmv'

    ALLOWED_HOSTS = []


    # Application definition

    INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'rest_framework_mongoengine',
    ]

    MIDDLEWARE_CLASSES = [
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'mongomine.urls'

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

    WSGI_APPLICATION = 'wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/1.9/ref/settings/#databases

    DATABASES = {
	'default': {
	    'ENGINE': 'django.db.backends.sqlite3',
	    'NAME': os.path.join(DJANGO_ROOT, 'db.sqlite3'),
	}
    }
