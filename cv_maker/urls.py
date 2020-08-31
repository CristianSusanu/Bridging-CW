from django.urls import path
from .views import HomeView, AddPersonalDetailsView, AddCareerProfile, AddWorkExperience, AddEducation, AddSkills, EditExperience, DeleteExperience, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="cv_home"),
    path('add_personal_details/', AddPersonalDetailsView.as_view(), name="add_personal_details"),
    path('add_career_profile/', AddCareerProfile.as_view(), name="add_career_profile"),
    path('add_work_experience/', AddWorkExperience.as_view(), name="add_work_experience"),
    path('add_education/', AddEducation.as_view(), name="add_education"),
    path('add_skills/', AddSkills.as_view(), name="add_skills"),
    path('edit_cv_post/<slug:pk>', EditExperience.as_view(), name="edit_cv_post"),
    path('delete_post/<slug:pk>', DeleteExperience.as_view(), name="delete_cv_post"),
    path('category/<str:cats>/', CategoryView, name="category"),
]
