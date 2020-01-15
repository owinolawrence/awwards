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


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    # serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)

    permission_classes = (IsAuthenticated,)

   

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()

    # serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


   

 
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    # serializer_class = ReviewSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)





def rate(request,pk):
    current_user = request.user
    post = Post.objects.get(pk=pk)
    review = Review.get_reviews(post.id)
    form = ReviewForm(request.POST)
 
    if request.method == 'POST':
        if form.is_valid:
            review = form.save(commit=False)
            review.user = current_user
            review.post = post
            review.post_id = post.id
            review.save()
            return redirect('home')

        else:
            form = ReviewForm()

    return render(request, 'review_form.html',{'form':form, 'post':post, 'comments':review})            






@login_required
def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})