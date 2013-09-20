from django.conf.urls import patterns, include, url

# API
from rest_framework import routers
from api.views import SessionView


router = routers.DefaultRouter()
# Register api endpoints to default router


urlpatterns = patterns('',
    #url(r'^$', 'api.views.api_root', name='api_root'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^session/', SessionView.as_view(), name='session'),
    url(r'', include(router.urls)),
)
