from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.main.urls', namespace="main")),
    url(r'^', include('apps.invoices.urls', namespace="invoice_app")),
    url(r'^', include('apps.users.urls', namespace="users")),
]

if settings.DEBUG :
	urlpatterns += [ 
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	]