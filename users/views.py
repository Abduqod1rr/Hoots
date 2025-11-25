from django.shortcuts import render 
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView 
from django.views.generic import CreateView ,ListView,UpdateView,DeleteView
from django.contrib.auth.models import User
from .forms import cuserform

class UserRegister(CreateView):
    model=User
    form_class=cuserform
    template_name='register.html'
    success_url=reverse_lazy('login')

class Userlogin(LoginView):
    template_name='login.html'
    success_url = reverse_lazy('home')




