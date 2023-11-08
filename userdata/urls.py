from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [ 
  
    
  path('register/', UserRegistration.as_view(), name='userregister'),
  # path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('register/',  RegisterView.as_view(), name='register'),
  path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

  path('dashboard/',views.dashboard, name='dashboard'),
  # path('usersblogs',views.UserBlog, name='usersblogs'),
  path('',views.LoginView, name='login'),
  path('adminblog/',views.AdminBlog, name='adminblog'),
  path('', UserRegistration.as_view(), name='userregister'),
  path('userlist/', ListUserview.as_view(), name='userlist'),
  path('userlist/<int:userId>/', ListUserview.as_view(), name='userlist')

]