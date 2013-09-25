import os
import sys
from os.path import abspath, dirname, join

PROJECT_NAME = 'djangobbb'
VE_BASE_PATH = '/home/ninjabit/dev/env'
PROJECT_BASE_PATH = '/home/ninjabit/dev/projects'

#VEpath = "/home/ninjabit/dev/env/labtest/lib/python2.7/site-packages"
VEpath = os.path.join(VE_BASE_PATH, PROJECT_NAME, '/lib/python2.7/site-packages')
PRJpath = os.path.join(PROJECT_BASE_PATH, PROJECT_NAME)

sys.path.insert(0, VEpath)
sys.path.insert(0, abspath(join(dirname(__file__), "../../")))

#path = '/home/ninjabit/dev/projects/labtest'
#if path not in sys.path:
if PRJpath not in sys.path:
    sys.path.insert(0, PRJpath)

#os.environ['DJANGO_SETTINGS_MODULE'] = 'labtest.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = PROJECT_NAME + '.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

