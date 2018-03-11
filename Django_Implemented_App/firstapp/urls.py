from django.conf.urls import url
from firstapp import views
urlpatterns = [
    url(r'^hello_firstapp$' , views.core_html, name='hello')
]