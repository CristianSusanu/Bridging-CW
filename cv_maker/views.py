from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Experience, Category
from .forms import ExperienceForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Experience
    template_name = 'cv_home.html'
    ordering = 'positioning'

class AddPersonalDetailsView(CreateView):
    model = Experience
    template_name = 'cv_add_personal_details.html'
    form_class = ExperienceForm

class AddCareerProfile(CreateView):
    model = Experience
    template_name = 'cv_add_career_profile.html'
    form_class = ExperienceForm

class AddWorkExperience(CreateView):
    model = Experience
    template_name = 'cv_add_work_experience.html'
    form_class = ExperienceForm

class AddEducation(CreateView):
    model = Experience
    template_name = 'cv_add_education.html'
    form_class = ExperienceForm

class AddSkills(CreateView):
    model = Experience
    template_name = "cv_add_skills.html"
    form_class = ExperienceForm

class EditExperience(UpdateView):
    model = Experience
    template_name = 'cv_update_post.html'
    form_class = ExperienceForm

class DeleteExperience(DeleteView):
    model = Experience
    template_name = 'cv_delete_post.html'
    success_url = reverse_lazy('cv_home')

def CategoryView(request, cats):
    category_posts = Experience.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats, 'category_posts': category_posts})
