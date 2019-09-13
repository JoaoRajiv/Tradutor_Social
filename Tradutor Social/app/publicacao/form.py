from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ['account', 'text_p', 'text_e']
    
class ComentForm(ModelForm):
    class Meta:
        model = Correction
        fields = ['corrector', 'publications', 'correction']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'age', 'scholarity']



        
