from django.conf.urls import patterns, url, include
from django.conf.urls.defaults import *
from tastypie.api import *
#from myproject.api.newuser import UsersResource, PagesResource
from myproject.api.newuser1 import UserResource, PageResource, PagesResource
#from myproject.views import first
from myproject.views import first1

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()
v1_api = Api(api_name='v1')
v2_api = Api(api_name='v2')
#v3_api = Api(api_name='v3')
#v1_api.register(UsersResource())
v2_api.register(UserResource())
v1_api.register(PageResource())
v1_api.register(PagesResource())
#v2_api.register(PagesResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
	(r'', include(v2_api.urls)),
	url(r'^user/$',first1.users12),
	(r'', include(v1_api.urls)),
	url(r'^user1/$',first1.users123),
	(r'', include(v1_api.urls)),
	url(r'^data/$',first1.users999),
)
