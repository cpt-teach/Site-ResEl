from django.shortcuts import render , redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import InscriptionForm


def userhome(request):
    if request.method == 'GET':
        return HttpResponse("Ceci est la page d'Accueil du sute d'utilisateur")
    elif request.method == 'POST':
        return HttpResponse("Ceci est la page d'Accueil du sute d'utilisateur")
    


def new_inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Ceci est la page d'Accueil du sute d'utilisateur")
    else:
        form = InscriptionForm()
    return render(request, "Inscription/new_inscription.html", {'form':form})
    