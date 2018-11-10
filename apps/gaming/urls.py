from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^pacman/$',views.pacman,name="pacman"),
    url(r'^airforceBattle/$',views.Airforce,name="Airforce"),
    url(r'^gameScore/$', views.gameScore, name="gameScore")
]