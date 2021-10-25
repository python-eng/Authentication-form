from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UsernameField
from django import forms
from django.core.checks.messages import Error
from django.forms import widgets
from django.forms.models import ModelForm
from myapplication.models import Singup
from django.utils.translation import gettext, gettext_lazy as _


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'login__input','placeholder':'Password'}),
     
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'login__input','placeholder':'Retype password'}),
        strip=False,
    )
    class Meta:
        model=Singup
        fields=['username','email','first_name','last_name','Address']

        widgets={
            'username':forms.TextInput(attrs={'class':'login__input','placeholder':'Username'}),
            'email':forms.EmailInput(attrs={'class':'login__input','placeholder':'Email'}),
            'first_name':forms.TextInput(attrs={'class':'login__input','placeholder':'First name'}),
            'last_name':forms.TextInput(attrs={'class':'login__input','placeholder':'Last name'}),
            'Address':forms.TextInput(attrs={'class':'login__input','placeholder':'Address'}),
            }

class LoginForm(AuthenticationForm):
      username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'login__input','placeholder':'Username'}))
      password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'login__input','placeholder':'Password'}),
    )


class UpdateForm(ModelForm):
    
    class Meta:
        model=Singup
        fields=['email','first_name','last_name','Address']
        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control','id':'email'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','id':'first_name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','id':'last_name'}),
            'Address':forms.TextInput(attrs={'class':'form-control','id':'address'}),
            }
        error_messages ={
            'email':{'required':'email field should not be empty'},
            'first_name':{'required':'first_name field should not be empty'},
            'last_name':{'required':'last_name field should not be empty'},
            'Address':{'required':'Address field should not be empty'},
        }
