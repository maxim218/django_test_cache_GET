from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^qqq/', views.qqq, name='qqq'),
    url(r'^qqq111/', views.qqq111, name='qqq111'),
    url(r'^qqq222/', views.qqq222, name='qqq222'),
]
