from django.conf.urls import url
from sites import views


urlpatterns = [

    url(r'^signup$' , views.signup, name='signup'),
    url(r'^signin$' , views.signin, name='signin'),
    url(r'^logoutfunction$' , views.logoutfunction, name='logoutfunction'),
    url(r'^dashboard$' , views.dashboard, name='dashboard'),
    url(r'^static_example$' , views.staticExample, name='static_example')

]