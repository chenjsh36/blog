from django.conf.urls import patterns, include, url
from myblog.testview import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
	(r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^account/logout/$', logout),
    (r'^account/login/$', login),
    (r'^(\d+)/$', article_search),
    (r'^personal/$', personal),
    (r'^personal/article/edit/(\d+)/$', article_edit),
    (r'^personal/article/del/(\d+)/$', article_del),
    (r'^personal/article/add/$', article_add),
    (r'^personal/articles/$', articles_show),
    # (r'^account/regist/$', regist),
	(r'^$', index),
	
)

# urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
# )
