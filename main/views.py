from django.shortcuts import render, HttpResponse
from django.shortcuts import render 
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView 
from django.views.generic import CreateView ,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hoots ,Following


class Homeview(ListView):
    model=Hoots
    template_name='home.html'
    context_object_name='hoots'

class createHoot(LoginRequiredMixin,CreateView):
    model = Hoots
    template_name = 'create_hoot.html'
    success_url = reverse_lazy('home'),
    fields=['title','hoot']

    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super().form_valid(form)
    