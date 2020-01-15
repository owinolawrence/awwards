from django.shortcuts import render,get_object_or_404,redirect,reverse,HttpResponseRedirect
from .models import *
from django.views.generic import DetailView,CreateView
from rest_framework import viewsets,status
from users.models import *
# from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer

import random
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    post = Post.objects.all()
    posts = post[::-1]
    landing = random.randint(0,len(post)-1)
    random_post = posts[landing]

    

    return render(request, 'index.html',{'post':post,'random_post':random_post})



class PostDetailView(DetailView):
    model = Post
    



class PostCreateView(CreateView):
    model = Post
    fields = ('__all__')

    def form_valid(self, form):
        form.instance.account_user= self.request.user
        form.instance.profile_user= Profile.objects.get(id=self.request.user.profile.id)
        

        form.save()


        return redirect('home')


