# -*- coding: utf-8 -*-
from split_settings.tools import optional, include


include(
    'components/base.py',
    'components/database.py',
    'components/authentication.py',
    'components/cms.py',
    'components/easy_thumbnails.py',
    'components/avatar.py',
    'components/registration.py',
    'components/admin_shortcuts.py',
    'components/debug_toolbar.py',
    'components/logger.py',
    optional('local_settings.py'),

    scope=locals()
)