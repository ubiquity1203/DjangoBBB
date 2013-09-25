# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from profiles.views import ProfileApiView


urlpatterns = patterns('',
                       url(r'^$', ProfileApiView.as_view(), name='profile-api'),
)