from django.test import TestCase, Client
from django.urls import reverse
from cv_maker.models import Experience, Category

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homeview_url = reverse('cv_home')
        self.addpersonaldetails_url = reverse('add_personal_details')
        self.addcareerprofile_url = reverse('add_career_profile')
        self.addworkexperience_url = reverse('add_work_experience')
        self.addeducation_url = reverse('add_education')
        self.addskills_url = reverse('add_skills')
        self.edit_url = reverse('edit_cv_post', args=['experience1'])

    def test_HomeView_GET(self):
        response = self.client.get(self.homeview_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cv_home.html')

    def test_AddPersonalDetailsView_GET(self):
        response = self.client.get(self.addpersonaldetails_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cv_add_personal_details.html')

    def test_AddCareerProfileView_GET(self):
        response = self.client.get(self.addcareerprofile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cv_add_career_profile.html')

    def test_AddWorkExperienceView_GET(self):
        response = self.client.get(self.addworkexperience_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cv_add_work_experience.html')

    def test_AddEducationView_GET(self):
        response = self.client.get(self.addeducation_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cv_add_education.html')

    def test_AddskillsView_GET(self):
        response = self.client.get(self.addskills_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cv_add_skills.html')
