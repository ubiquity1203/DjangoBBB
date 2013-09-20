# -*- coding: utf-8 -*-
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # GUARDIAN
    'guardian.backends.ObjectPermissionBackend',
    #'profile.backends.EmailAuthBackend',
)

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# LOGIN_URL = '/login'
# LOGOUT_URL = '/logout'

# GUARDIAN
ANONYMOUS_USER_ID = -1