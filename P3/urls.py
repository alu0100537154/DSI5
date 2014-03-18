from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'P3.estaticas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
url(r'^home', 'estaticas.views.home'),
url(r'^about', 'estaticas.views.about'),
url(r'^help', 'estaticas.views.help'),


)
