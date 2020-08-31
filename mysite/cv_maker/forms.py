from django import forms
from django.forms import ModelForm
from .models import Experience, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('category', 'text')

        widgets = {
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control'}),
        }
