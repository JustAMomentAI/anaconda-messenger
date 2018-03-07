from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.loginPage, name = "index"),
    url(r'^home/', views.homePage, name = "home")
]