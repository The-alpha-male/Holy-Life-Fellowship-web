from pyexpat import model
from django import forms
from . models import Contactus
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data
class contactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ['full_name', 'email', 'phone', 'message']
        
        
class loginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ['username', 'password']