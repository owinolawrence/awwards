from django.test import TestCase
from .models import *
import unittest
from django.contrib.auth.models import User
# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.post = Post(title='title',live_link='sfggfdsgedgfgfd',description ='sdfdsad',country='dasfsdfasdf',languages='sfsafsasfa',landing_page = 'media/img.jpeg',screenshot_one = 'media/img.jpeg',screenshot_two = 'media/img.jpeg',screenshot_three = 'media/img.jpeg',screenshot_four = 'media/img.jpeg',date_posted='hhhjjhjhh')


    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))


class TestReview(TestCase):
    def setUp(self):
        self.review = Review(design=1,usability=1,content=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.review,Review))   