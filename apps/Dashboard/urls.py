from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.homePage, name="homePage"),
    url(r'^profile_Page/(?P<user_id>\d+)$', views.profile, name="profile"),
    url(r'^find_friends/$', views.find_friends, name="find_friends"),
    url(r'^searchFriends/$', views.searchFriends, name="searchFriends"),
    url(r'^searchPostByName/$', views.searchPostByName, name="searchPostByName"),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)