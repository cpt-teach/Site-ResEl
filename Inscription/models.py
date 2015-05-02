from django.db import models

class User(models.Model):
    Nom= models.CharField(max_length=30)
    Prenom= models.CharField(max_length=30)
    
