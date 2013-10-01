# -*- coding: utf-8 -*-
CORS_ORIGIN_ALLOW_ALL = True # default False
CORS_ORIGIN_WHITELIST = (
    'ninjabit.com',
) # default ()
CORS_ORIGIN_REGEX_WHITELIST = ('^http?://(\w+\.)?ninjabit\.com$', ) # default ()
CORS_PREFLIGHT_MAX_AGE = 86400 # default