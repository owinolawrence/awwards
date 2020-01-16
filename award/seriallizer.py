from rest_framework import serializers
from .models import *
from users.models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','live_link','description','languages','profile_user','landing_page','date_posted','user']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'        
