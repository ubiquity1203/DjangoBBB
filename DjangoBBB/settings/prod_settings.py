### USAGE ###
# Enable
# ENV = 'prod'
# in main settings.py


#############################
#           ENV             #
#############################
DEBUG = False
TEMPLATE_DEBUG = DEBUG


#############################
#          DB-PROD          #
#############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'labtest', # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'labtest',
        'PASSWORD': 'labtestpwd',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


#############################
#          LOCALE           #
#############################
LOCALE_PATHS = (
    '/home/ninjabit/dev/projects/labtest/locale',
)


#############################
#          PATHS            #
#############################
MEDIA_ROOT = "/home/ninjabit/labtest.ninjabit.com/"
STATIC_ROOT = "/home/ninjabit/labtest.ninjabit.com"
