from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cv_maker.views import HomeView, AddPersonalDetailsView, AddCareerProfile, AddWorkExperience
from cv_maker.views import AddEducation, AddSkills, EditExperience, DeleteExperience, CategoryView

class TestUrls(SimpleTestCase):

    def test_cv_home_url_is_resolved(self):
        url = reverse('cv_home')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_add_personal_details_view_url_is_resolved(self):
        url = reverse('add_personal_details')
        self.assertEquals(resolve(url).func.view_class, AddPersonalDetailsView)

    def test_add_career_profile_view_url_is_resolved(self):
        url = reverse('add_career_profile')
        self.assertEquals(resolve(url).func.view_class, AddCareerProfile)

    def test_add_work_experience_view_url_is_resolved(self):
        url = reverse('add_work_experience')
        self.assertEquals(resolve(url).func.view_class, AddWorkExperience)

    def test_add_education_view_url_is_resolved(self):
        url = reverse('add_education')
        self.assertEquals(resolve(url).func.view_class, AddEducation)

    def test_add_skills_view_url_is_resolved(self):
        url = reverse('add_skills')
        self.assertEquals(resolve(url).func.view_class, AddSkills)

    def test_edit_experience_view_url_is_resolved(self):
        url = reverse('edit_cv_post', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, EditExperience)

    def test_delete_experience_view_url_is_resolved(self):
        url = reverse('delete_cv_post', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, DeleteExperience)

    def test_category_view_url_is_resolved(self):
        url = reverse('category', args=['some-slug'])
        self.assertEquals(resolve(url).func, CategoryView)
