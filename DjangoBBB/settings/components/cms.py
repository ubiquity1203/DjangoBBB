CMS_TEMPLATES = (
    ('home_page.html', 'Home page'),
    ('internal_page.html', 'Internal page'),
)

gettext = lambda s: s

LANGUAGES = [
    ('en', gettext('English')),
    ('it', gettext('Italian')),
    ('fr', gettext('French')),
]

MENU_CACHE_DURATION = 0
CMS_PERMISSION = True