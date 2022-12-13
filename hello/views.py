from django.shortcuts import render
from django.views.generic import ListView
from .models import HelloModel
# Create your views here.

class HelloView(ListView):
    model = HelloModel
    template_name = "hello.html" 