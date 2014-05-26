from django.conf.urls import patterns, include, url
from django.contrib import admin
from customer import views

urlpatterns = [

    url(r'^customer_list/$', views.customer_list, name='customer_list'),
    url(r'^customer/(?P<id>\d+)', views.customer_view, name='customer'),
    url(r'^customer_create/$', views.customer_create, name='customer_add'),
    url(r'^customer_update/(?P<id>\d+)$', views.customer_update, name='customer_update'),
    url(r'^customer_delete/(?P<id>\d+)$', views.customer_delete, name='customer_delete'),

    url(r'^meeting_list/$', views.meeting_list, name='meeting_list'),
    url(r'^meeting/(?P<id>\d+)$', views.meeting_view, name='meeting'),
    url(r'^meeting_create/(?P<id>\d+)$', views.meeting_create, name='meeting_add'),
    url(r'^meeting_update/(?P<id>\d+)$', views.meeting_update, name='meeting_update'),
    url(r'^meeting_delete/(?P<id>\d+)$', views.meeting_delete, name='meeting_delete'),

]

