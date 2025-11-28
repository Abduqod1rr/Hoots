from django.shortcuts import render, HttpResponse
from django.shortcuts import render ,get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView 
from django.views.generic import CreateView ,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hoots ,Following
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class Homeview(ListView):
    model=Hoots
    template_name='home.html'
    context_object_name='hoots'

class createHoot(LoginRequiredMixin,CreateView):
    model = Hoots
    template_name = 'create_hoot.html'
    success_url = reverse_lazy('home')
    fields=['title','hoot']

    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super().form_valid(form)

class myhootsview(ListView):
    model=Hoots
    template_name='myhoots.html'
    context_object_name='hoots'

    def get_queryset(self):
        return Hoots.objects.filter(owner=self.request.user) 
    


class deleteHoot(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Hoots
    template_name='delete_hoot.html'
    success_url=reverse_lazy('home')
    context_object_name='hoots'

    def test_func(self):
        obj=self.get_object()
        return self.request.user == obj.owner
    
class updateHoot(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Hoots
    fields=['title','hoot']
    template_name='create_hoot.html'
    success_url = reverse_lazy('myhoots')
    context_object_name='hoots'
    

    def test_func(self):
        obj=self.get_object()
        return self.request.user == obj.owner