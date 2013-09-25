from django.conf.urls import patterns, include, url
from rest_framework import routers
from api.views import SessionView, APIRoot
from profiles.views import ProfileApiView


# API

router = routers.DefaultRouter()
# Register api endpoints to default router

urlpatterns = patterns('',
                       url(r'^$', APIRoot.as_view(), name='api_root'),
                       url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^session/', SessionView.as_view(), name='session'),
                       #url(r'^profile/', ProfileApiView.as_view(), name='profile-api'),
                       #url(r'', include(router.urls)),
)
