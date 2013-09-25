# -*- coding: utf-8 -*-
from django.conf import LazySettings

settings = LazySettings()


def title(request):
    if settings.SITE_TITLE:
        return {'TITLE': settings.SITE_TITLE}
    elif settings.PROJECT_NAME:
        return {'TITLE': settings.PROJECT_NAME}
    else:
        return {'TITLE': 'DefaultSiteTitle'}