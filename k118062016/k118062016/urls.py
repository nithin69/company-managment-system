from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from myproject import views, models
#from material.frontend import urls as frontend_urls
import notifications.urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'k118062016.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'', include(frontend_urls)),
    #url(r'^grappelli/', include('grappelli.urls')),
    #url(r'^jet/', include('jet.urls', 'jet')),
    #url(r'^tracking/', include('tracking.urls')),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    #url(r'^chat/', include('chatrooms.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('myproject.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    #url(r'^biodata/$', views.my_view, name='my_view'),
    #url(r'^advsearch/$', views.advsearch, name='advsearch'),
    url(r'^media/(?P<path>.*)/$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)

if settings.DEBUG:
	urlpatterns += patterns('',
                 (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
            )

        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)/$',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )
