from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^Accueil/', include('Accueil.urls')),
    url(r'^Inscription/', include('Inscription.urls')),
    url(r'^admin/',include(admin.site.urls)),
)