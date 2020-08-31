from django.db import models
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title #in the admin page see post

    def get_absolute_url(self):
        return reverse('home')
