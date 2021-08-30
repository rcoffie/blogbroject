from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import *
from django.contrib.auth import authenticate, login


class RegistrationForm(UserCreationForm):
  username = forms.CharField()
  email    = forms.EmailField()
  password1 = forms.CharField(label="Enter Password",widget=forms.PasswordInput)
  password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
  
  
  class Meta:
    model = Account 
    fields = ('username','email','password1','password2')
    
  def cleaned_email(self):
    email = self.cleaned_data['email']
    try:
      account = Account.objects.get(email=email)
    except Exception as e:
      raise forms.ValidationError(f'email {email} has already been taken')
  
  def cleaned_username(self):
    username = self.cleaned_data['username']
    try:
      account = Account.objects.get(username=username)
    except Exception as e:
      raise forms.ValidationError(f'username {username} already exists')
    
    
 
            

            
class LoginForm(forms.Form):
  email = forms.EmailField(label='Email',widget=forms.EmailInput())
  password = forms.CharField(label="password",widget=forms.PasswordInput(attrs={'placeholder':'password'}))
  
  def clean(self):
    if self.is_valid():
      email = self.cleaned_data['email']
      password = self.cleaned_data['password']
      if not authenticate(email=email, password=password):
        raise forms.ValidateError("invalid login check your credentials ")



class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile 
    fields = ['body','twitter','facebook','github','profile_picture']
    
    
    
    
class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()
  
  class Meta:
    model = Account 
    fields = ['username','email']