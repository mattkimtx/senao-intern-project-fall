from django.shortcuts import render
from django.views import generic

# Create your views here.

class loginView(generic.ListView):
    template_name = "login/login.html"
    context_object_name = "login"
    