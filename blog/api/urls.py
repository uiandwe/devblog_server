from django.conf.urls import url
from django.contrib import admin

from .views import (
    BlogCreateAPIView,
    BlogListAPIView,
    BlogDetailAPIView,
    BlogUpdateAPIView,
    BlogDeleteAPIView,
)


urlpatterns = [
    url(r'^$', BlogListAPIView.as_view(), name='list'),
    url(r'^create/$', BlogCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', BlogDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', BlogUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', BlogDeleteAPIView.as_view(), name='delete'),

]