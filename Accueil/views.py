from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request,'Accueil/index.html',locals())

def Contacts(request):
    return render(request,'Accueil/contact.html',locals())