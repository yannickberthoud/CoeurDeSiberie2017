"""
Definition of urls for CoeurDeSiberie.
"""

from datetime import datetime
import django.contrib.auth.views

from django.conf import settings
from django.conf.urls.static import static


from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from CoeurDeSiberie.views import  home, contact

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^chats-de-siberie/', include('cat.urls', namespace = 'cats')),
    url(r'^nos-serpents/', include('snake.urls', namespace = 'snakes')),
    url(r'^contact/', contact, name='contact'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)