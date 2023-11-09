from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [ 
  
    
  path('register/', UserRegistration.as_view(), name='userregister'),
  
  path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

  path('dashboard/',views.dashboard, name='dashboard'),
  path('reg/',views.RegisterView, name='reg'),
  path('',views.LoginView, name='login'),
  path('adminblog/',views.AdminBlog, name='adminblog'),
 
  path('userlist/', ListUserview.as_view(), name='userlist'),
  path('userlist/<int:userId>/', ListUserview.as_view(), name='userlist')

]