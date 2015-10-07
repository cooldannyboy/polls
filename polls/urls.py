from django.conf.urls import patterns, include, url
from django.contrib import admin

#from polls_app.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'polls.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls_app/', include('polls_app.urls', namespace="polls_app")),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^test/$', index),
)
