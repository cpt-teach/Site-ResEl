from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('Acceuil.views',
    url(r'^home$', 'home'),  # Accueil du Site
    url(r'^contacts$', 'Contacts'),  # Contacts du site
   
)