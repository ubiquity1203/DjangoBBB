from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.http.response import HttpResponseNotFound, HttpResponseServerError
from django.views.generic.base import TemplateView

admin.autodiscover()

# ADMIN
urlpatterns = patterns('',
                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
)

# AUTH
urlpatterns += i18n_patterns('',
                             # Registration urls
                             url(r'^accounts/', include('registration.backends.default.urls')),
)

# HOME
urlpatterns += i18n_patterns('',
                             url(r'^$', TemplateView.as_view(template_name='index.html'), name='index')
)


#########################################
#                                       #
#                DEBUG                  #
#                                       #
#########################################
## Served from nginx proxy in test and prod
if settings.DEBUG:
    urlpatterns = patterns('',
                           url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                           url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns

## Rosetta urls
if settings.DEBUG:
    if 'rosetta' in settings.INSTALLED_APPS:
        urlpatterns += patterns('',
                                url(r'^rosetta/', include('rosetta.urls')),
        )

## Error page test urls
if settings.DEBUG:
    urlpatterns = patterns('',
                           url(r'^test404/', HttpResponseNotFound),
                           url(r'^test500/', HttpResponseServerError),
) + urlpatterns