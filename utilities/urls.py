from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.loginPage, name = "index"),
    url(r'^home/$', views.homePage, name = "home"),
    #url(r'^messages/$', views.updateMessages, name = "message")
    url(r'^meetings', views.goToSetMeetingsAndIdeas, name = "generate")
]