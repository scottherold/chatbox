from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index, name="index"),
    url(r'^create/(?P<user_id>\d+)$', views.create, name="create"),
     url(r'^destroy/(?P<user_id>\d+)/$', views.delete, name="delete"),



    url(r'^new/$', views.new, name="new"),
    url(r'^(?P<id>\d+)/edit/$', views.edit, name="edit"),
    url(r'^(?P<id>\d+)/$', views.show, name="show"),
]