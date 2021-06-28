from django.conf.urls import url

from . import views

# app_name = 'bunks' I don't want to deal with this
urlpatterns = [
    # bunks
    url(r'^$', views.index, name='index'),
    # bunks/Sydney
    url(r'^(?P<username>\w+)/$', views.detail, name='detail'),
    url(r'^(?P<username>\w+)/bunk/$', views.makeBunk, name='makeBunk'),
]