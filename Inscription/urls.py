from django.conf.urls import patterns, include, url

urlpatterns = patterns('Inscription.views',
    url(r'^new_inscription$', 'new_inscription'),  # Nouvelle inscription
    url(r'^userhome$', 'userhome'),
   
)