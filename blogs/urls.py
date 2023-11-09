from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [ 
  
  path('blogadds',views.AddBlog, name='blogadds'),
  path('addblog/', AdminAddBlogs.as_view(), name='addblog'),
  path('updateblog/<int:blogId>/',UpdateBlogPost.as_view(), name='updateblog'),
  path('addcomment/', views.add_comment, name='addcomment'),
  # path('upblog/<int:blogId>/',  UpdateView.as_view(), name='upblog'),   

  path('deleteblog/<int:blogId>/', views.DeleteBlog, name='deleteblog'),
  path('home/',views.UserHome, name='home'),
  path('getcomment/<int:post_id>/', views.GetComments.as_view(), name='getcomment'),
  path('likepost/<int:post_id>/', views.LikeorDislike, name='likepost'),


  path('logout/', views.UserLogoutAPIView.as_view(), name='logout'),
]
