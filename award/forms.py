from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post


class UserRegestrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User

        fields = ['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User

        fields = ['username','email']    


class ProfileUpdateForm(forms.ModelForm):



    class Meta:
        model = Profile

        fields = ['image']   

class ReviewForm(forms.ModelForm):



    class Meta:
        model = Profile

        fields = ['image']   

class CreatePostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'live_link', 'description', 'country', 'languages', 'landing_page', 'screenshot_one', 'screenshot_two')