from django.http.request import validate_host
from django.urls import path
from . import views


app_name = 'indexurl'
urlpatterns = [
path('',views.myindex, name ='index'),
path('about/',views.myabout, name ='about'),
path('contact/',views.mycontact, name ='contact'),
path('services/',views.myservices, name='services'),
path('track/',views.mytrack, name='track'),

		]