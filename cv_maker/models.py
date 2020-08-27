from django.db import models
from django.urls import reverse

# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.title #in the admin page see post

        #def get_absolute_url(self):
        #    return reverse('home')
