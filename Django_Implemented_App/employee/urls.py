from django.conf.urls import url
from employee import views
urlpatterns = [

    url(r'^hello_employee$' , views.helloemployee, name='helloemployee')
]