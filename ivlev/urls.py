from django.conf.urls import patterns, include, url
from apps.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ivlev.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^crossdomain.xml', 'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT, 'path': 'crossdomain.xml'}),
    (r'^' + settings.MEDIA_URL[1:] + '(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^apps/', include('apps.urls')),

    # url(r'^/'),
)


if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^static/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
        )
    urlpatterns += patterns('',
                 (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
            )
