from django.conf.urls.defaults import *
from core.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
     (r'^$', index),
     (r'add_person/', add_person),
     (r'edit_person/', edit_person),
     (r'settings/', settings),
     (r'first10items/', first10items),
     (r'^accounts/login/$', 'django.contrib.auth.views.login',
                                        {'template_name': 'login.html'}),


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
