from django.conf.urls import patterns, include, url
from django.contrib import admin

import pointstracker.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flyerdr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += pointstracker.urls.urlpatterns

