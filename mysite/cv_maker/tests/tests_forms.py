from django.test import SimpleTestCase
from cv_maker.forms import ExperienceForm

class TestForms(SimpleTestCase):

    def test_experienceform(self):
        form = ExperienceForm(data={
            'category': 'Skills',
            'text': 'computer coding'
        })

        self.assertTrue(form.is_valid())

    def test_experienceform_no_data(self):
        form = ExperienceForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
