from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^register/$',views.register,name='registration'),
    url(r'^create/$', views.create, name="create"),
    url(r'^loginProccess',views.LoginProccess,name='LoginProccess'),
    url(r'^login/$', views.login, name="login"),
    # url(r'^pokes/$', views.pokes, name="pokes"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^update/(?P<user_id>\d+)$', views.update, name="update"),

]

