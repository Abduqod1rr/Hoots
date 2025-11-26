from django.shortcuts import render, HttpResponse
from django.shortcuts import render 
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView 
from django.views.generic import CreateView ,ListView,UpdateView,DeleteView
from .models import Hoots ,Following


class Homeview(ListView):
    model=Hoots
    template_name='home.html'