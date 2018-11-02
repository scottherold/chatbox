from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homePage, name="homePage"),
    url(r'^profile_Page/(?P<user_id>\d+)$', views.profile, name="profile")

]