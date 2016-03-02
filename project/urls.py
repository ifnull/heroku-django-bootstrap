from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import apps.hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', apps.hello.views.index, name='index'),
    url(r'^db', apps.hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
