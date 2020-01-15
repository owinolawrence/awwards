from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile
from django.urls import reverse
import datetime
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator
from math import *

My_choices = (
    ('Django','Django'),
    ('Flask','Flask'),
    ('Python','Python'),
    ('Bootstrap','Bootstrap'),
    ('Material-Design','Material-Design'),
    ('Angular','Angular'),
    ('Html','Html'),
    ('Java-Script','Java-Script'),
    ('Java','Java'),
    ('Ruby','Ruby'),
    
    )

CHOICES = (1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)





class Post(models.Model):

    # profile_user = models.ForeignKey(Profile,on_delete=models.CASCADE,to_field=None)
    title = models.CharField(max_length = 30)
    live_link = models.URLField()
    description = models.TextField()
    country = CountryField()   

    languages = MultiSelectField(choices= My_choices)


    landing_page = models.ImageField(upload_to = 'media/images')
    screenshot_one = models.ImageField(upload_to = 'media/images')
    screenshot_two = models.ImageField(upload_to = 'media/images')


    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    date_posted = models.DateField(auto_now_add=True) 



    class Meta:
        ordering = ['-date_posted']
    

    def __str__(self):
        return self.title





    def get_absolute_url(self):
        return reverse('home',kwargs={'date_posted':self.date_posted})


    @classmethod
    def get_post(cls,title):
        post = cls.objects.filter(title__icontains = title)
        return post


