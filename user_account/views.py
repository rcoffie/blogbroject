from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .forms import LoginForm
from django.contrib import messages,auth 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.



def Registration(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,'account created successfully')
      return redirect('blog_post:home')
  else:
    form = RegistrationForm()
  context = {'form':form}
  return render(request,'user_account/register.html',context)  




def Login(request):
  form = LoginForm()
  if request.POST:
    form = LoginForm(request.POST)
    if form.is_valid():
      email = request.POST['email']
      password = request.POST['password']
      user = authenticate(email=email,password=password)
      if user:
        login(request, user)
        return redirect('blog_post:home')
  context = {'form':form}
  return render(request,'user_account/login.html',context)




def UserLogout(request):
  logout(request)
  return redirect('blog_post:home')