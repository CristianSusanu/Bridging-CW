from django.test import TestCase
from django.urls import reverse
from cv_maker.models import Experience, Category
from cv_maker.forms import ExperienceForm

class ModelTest(TestCase):

    def create_experience(self, title="test", text="This is only a test", category="Skills", positioning="5"):
        return Experience.objects.create(title=title, text=text, category=category, positioning=positioning)

    def create_category(self, name="Education", index="2"):
        return Category.objects.create(name="Education", index="2")

    def test_experience_model_creation(self):
        e = self.create_experience()
        self.assertTrue(isinstance(e, Experience))
        self.assertEqual(e.__str__(), e.title)
        self.assertEqual(e.get_absolute_url(), reverse('cv_home'))
        self.assertEqual(e.text, "This is only a test")
        self.assertEqual(e.category, "Skills")
        self.assertEqual(e.positioning, "5")

    def test_category_model_creation(self):
        c = self.create_category()
        self.assertTrue(isinstance(c, Category))
        self.assertEqual(c.__str__(), c.name)
        self.assertEqual(c.get_absolute_url(), reverse('cv_home'))
        self.assertEqual(c.name, "Education")
        self.assertEqual(c.index, "2")
