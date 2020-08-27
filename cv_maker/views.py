from django.shortcuts import render
from django.views.generic import ListView
from .models import Experience

class HomeView(ListView):
    model = Experience
    template_name = 'cv_home.html'
