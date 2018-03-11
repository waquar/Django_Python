from django.conf.urls import url , include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('firstapp.urls')),
    url(r'', include('employee.urls')),
    url(r'', include('indexapp.urls')),
    url(r'', include('sites.urls'))
]
