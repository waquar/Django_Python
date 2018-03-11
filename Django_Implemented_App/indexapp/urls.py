from django.conf.urls import url
from indexapp import views


urlpatterns = [

    url(r'^hello_index$' , views.create, name='create'),
    url(r'^view_index$' , views.index, name='index'),
    url(r'^update/(?P<pk>[0-9]+)$' , views.update, name='update'),
    url(r'^delete/(?P<pk>[0-9]+)$' , views.delete, name='delete'),
    url(r'^view/(?P<pk>[0-9]+)$' , views.views, name='view'),
    url(r'^create_customer$' , views.create_customer, name='create_customer'),
    url(r'^customer_index$' , views.customer_index, name='customer_index'),
    url(r'^updating_customer/(?P<pk>[0-9]+)$' , views.update_customer, name='updating_customer'),

]