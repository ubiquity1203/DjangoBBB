# -*- coding: utf-8 -*-
gettext = lambda s: s

ADMIN_SHORTCUTS = [
    {
        'title': gettext('Site'),
        'shortcuts': [
            {
                'title': gettext('View Site'),
                'url': '/',
                'open_new_window': True,
            },
        ]
    },
    {
        'title': 'API',
        'shortcuts': [
            {
                'title': gettext('API List'),
                'url': '/api',
                'open_new_window': True,
            },
        ]
    },
]