from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request,'Acceuil/index.html',locals())

def Contacts(request):
    return render(request,'Acceuil/contact.html',locals())