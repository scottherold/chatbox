from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^like_Post/(?P<post_id>\d+)/(?P<location>\w+)$',views.like_Post, name='like_Post'),
    url(r'^like_Comment/(?P<comment_id>\d+)/(?P<location>\w+)$',views.like_Comment, name='like_Comment')
]