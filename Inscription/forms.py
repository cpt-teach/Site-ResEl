from django.forms import ModelForm
from .models import User

class InscriptionForm(ModelForm):
    class Meta:
        model = User