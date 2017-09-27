from django.conf.urls import url

from .views import HomeView, DetailsView, fiche, jut

urlpatterns = [
    url(r'^$', HomeView.as_view(), name = 'home'),
    url(r'^le-siberien/$', fiche, name = 'fiche'),
    url(r'^la-saillie/$', jut, name='jut'),
    url(r'^(?P<slug>[\w-]+)/$', DetailsView.as_view(), name = 'details'),
]
