from django.shortcuts import render
from . models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

# Create your views here.


class UserList(ListView):
    model = User
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'


class UserDetail(DetailView):
    model = User
    template_name = 'accounts/user_detail.html'
    context_object_name = 'users'

class UserCreate(CreateView):
    model = User
    template_name = 'accounts/user_create.html'
    fields = ["name", "surname", "user_name", "password"]
    success_url = "accounts/"  

class UserUpdate(UpdateView):
    model = User
    template_name = 'accounts/user_update.html'
    fields = ["name", "surname", "user_name", "password"]
    success_url = "accounts/" 

class UserDelete(DeleteView):
    model = User
    template_name = 'accounts/user_delete.html'
    success_url = "accounts/" 