from django.conf.urls.defaults import *
from core.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
     (r'^$', index),
     (r'add_person/', add_person),
     (r'edit_person/', edit_person),
     (r'settings/', settings),
     (r'first10items/', first10items),
     (r'customtag/', customtag),
     (r'^accounts/login/$', 'django.contrib.auth.views.login',
                                        {'template_name': 'login.html'}),
     (r'^admin/', include(admin.site.urls)),
)
