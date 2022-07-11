from pyexpat import model
from django import forms
from . models import Contactus

class contactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ['full_name', 'email', 'phone', 'message']
