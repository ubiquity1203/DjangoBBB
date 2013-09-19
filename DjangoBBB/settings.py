# -*- coding: utf-8 -*-
import os
import glob


#############################
#           ENV             #
#############################
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ENV = 'Development'
#ENV = 'test'
#ENV = 'prod'

gettext = lambda s: s

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_NAME = os.getcwd().split(os.sep)[-1]

TEMPLATE_DEBUG = DEBUG


#############################
#          ADMINS           #
#############################
# Configured in local_settings
ADMINS = ()

MANAGERS = ADMINS


#############################
#          DB-DEV           #
#############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_PATH, 'database.sqlite'), # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


#############################
#          HOSTS-DEV        #
#############################
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

INTERNAL_IPS = ('127.0.0.1',)

SITE_ID = 1

# Make this unique, and don't share it with anybody.
# Configured in local_settings
SECRET_KEY = ''


#############################
#          LOCALE           #
#############################
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Rome'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'it-IT'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, "locale"),
)

#############################
#          PATHS            #
#############################
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, "static_root")

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, "static"),
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, "templates"),
)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'


#############################
#         LOADERS           #
#############################
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)


#############################
#        MIDDLEWARE         #
#############################
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # DEBUG TOOLBAR
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # DJANGO CMS
    'django.middleware.doc.XViewMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)


#############################
#        PROCESSORS         #
#############################
# TEMPLATE_CONTEXT_PROCESSORS
# THUMBNAIL_PROCESSORS
# Inspect the default values before configuring this setting
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    # SEKIZAI
    'sekizai.context_processors.sekizai',
    # DJANGO CMS
    'cms.context_processors.media',
)


#############################
#         PROJECT           #
#############################
ROOT_URLCONF = 'DjangoBBB.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'DjangoBBB.deploy.wsgi.application'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'


#############################
#           APPS            #
#############################
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ADMIN SHORTCUTS
    'admin_shortcuts',
    # ADMIN STYLE
    'djangocms_admin_style',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    # EASY THUMBNAILS
    'easy_thumbnails',
    # RESTFRAMEWORK
    'rest_framework',
    # DJANGO CMS
    'cms',
    'mptt',
    'menus',
    # SEKIZAI
    'sekizai',
    # MODELTRANSLATION
    'modeltranslation',
    # SOUTH
    'south',
    # DEBUG TOOLBAR
    'debug_toolbar',
    # PROJECT APPS

)


#############################
#          CONFS            #
#############################
# To keep settings minimal and usable
# other settings file are placed into conf/ path as .conf files
# Loading other settings
settingsfiles = glob.glob(os.path.join(os.path.dirname(__file__), 'conf', '*.conf.py'))
settingsfiles.sort()
for f in settingsfiles:
    try:
        execfile(os.path.abspath(f))
    except NameError:
        print('Exception executing file: %s'% f)

# Loading local settings
try:
    from local_settings import *
except ImportError:
    pass
# Loading test/prod settings based on ENV settings
if ENV == 'test':
    try:
        from test_settings import *
    except ImportError:
        pass
elif ENV == 'prod':
    try:
        from prod_settings import *
    except ImportError:
        pass
