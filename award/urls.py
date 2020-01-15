from django.conf.urls import url,include


from . import views 


urlpatterns=[
    url('^$',views.index, name= 'index'),
    url(r'^search/', views.search_results, name='search_results'),
    url('detail/(?P<pk>\d+)/',views.PostDetailView.as_view(), name ='post-detail'),
    url('post/new/',views.PostCreateView.as_view(), name ='post-create'),
    url (r'^search/',views.search_results,name= 'search_results'),    
    url('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url('post/review/(?P<post_id>\d+)',views.rate, name ='post-review'),    

]
