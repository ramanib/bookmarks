import os.path
from django.conf.urls.defaults import *
from bookmarks.views import *


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
#admin.autodiscover()

site_media = os.path.join(
os.path.dirname(__file__), 'site_media')


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^django_bookmarks/', include('django_bookmarks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_page),
    url(r'^user/(\w+)/$', user_page),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media }),
    url(r'^register/$', register_page),
  
)
