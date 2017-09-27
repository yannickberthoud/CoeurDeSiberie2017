#-*- coding: utf-8 -*-
from django.conf.urls import url

from .views import HomeView, DetailsView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name = 'home'),
    url(r'^(?P<slug>[\w-]+)-(?P<pk>\d+)/$', DetailsView.as_view(), name = 'details'),
]
