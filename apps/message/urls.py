from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^createComment/(?P<post_id>\d+)$', views.createComment, name="createComment"),
    url(r'^createPost/$', views.createPost, name="createPost"),
    url(r'^createReply/(?P<comment_id>\d+)$', views.createReply, name="createReply"),
    url(r'^delete/(?P<post_id>\d+)$', views.delete, name="delete"),
    

]