from selenium import webdriver
from django.urls import reverse
import unittest

class HomeViewTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_HomeView(self):
        self.browser.get('http://localhost:8000/resume/')
        self.assertIn('CV', self.browser.title)

    def test_personal_details_view(self):
        self.browser.get('http://localhost:8000/resume/add_personal_details')

        text = self.browser.find_element_by_tag_name('h1')
        text2 = self.browser.find_element_by_tag_name('h4')

        self.assertIn('Add Personal Details', self.browser.title)
        self.assertTrue(text, "Personal Details")
        self.assertTrue(text2, "Please Input your Name, Email Address and Phone Number")

    def test_career_profile_view(self):
        self.browser.get('http://localhost:8000/resume/add_career_profile')

        text = self.browser.find_element_by_tag_name('h1')
        text2 = self.browser.find_element_by_tag_name('h4')

        self.assertTrue(text, "Add Career Profile")
        self.assertTrue(text2, "Please provide a short description of yourself.")
        self.assertIn('Add Career Profile', self.browser.title)

    def test_work_experience_view(self):
        self.browser.get('http://localhost:8000/resume/add_work_experience')

        text = self.browser.find_element_by_tag_name('h1')
        text2 = self.browser.find_element_by_tag_name('h4')

        self.assertTrue(text, "Add Work Experience")
        self.assertTrue(text2, "Please provide any relevant work experience.")
        self.assertIn('Add Work Experience', self.browser.title)

    def test_education_view(self):
        self.browser.get('http://localhost:8000/resume/add_education')

        text = self.browser.find_element_by_tag_name('h1')
        text2 = self.browser.find_element_by_tag_name('h4')

        self.assertTrue(text, "Add Education Details")
        self.assertTrue(text2, "Please add Education Details.")
        self.assertIn('Add Education Details', self.browser.title)

    def test_skills_view(self):
        self.browser.get('http://localhost:8000/resume/add_skills')

        text = self.browser.find_element_by_tag_name('h1')
        text2 = self.browser.find_element_by_tag_name('h4')

        self.assertTrue(text, "Add Skills")
        self.assertTrue(text2, "Please provide any relevant skills.")
        self.assertIn("Add Skills", self.browser.title)

    def test_category_view(self):
        self.browser.get('http://localhost:8000/resume/category/slugs')

        text = self.browser.find_element_by_tag_name('h2')

        self.assertTrue(text, "Sorry, this page does not exit. Please enter a valid Url.")
        self.assertIn("Categories", self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
