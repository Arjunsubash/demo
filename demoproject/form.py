from django import forms
from django.forms import ModelForm
# from Teams.models import Register
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Loginform(forms.Form):    
    username = forms.CharField(label='username', max_length=100, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'Username'}),)
               
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput({'class': "form-control",'placeholder': 'Password'}))
    def clean(self):
        cleaned_data = super(Loginform, self).clean()
        username = cleaned_data.get('username') 
        password = cleaned_data.get('password')
        if len(username) < 3: 
            #raise forms.ValidationError("minimum 5 characters")
            msg="Minimum 3 characters required"
            self.add_error('username', msg)
        if len(password) < 3: 
            #raise forms.ValidationError("minimum 5 characters")
            msg="Minimum 3 characters required"
            self.add_error('password', msg) 
        return self.cleaned_data

