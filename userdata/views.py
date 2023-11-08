from rest_framework.response import Response
from rest_framework import status
from .models import AppUsers
from rest_framework.generics import ListAPIView ,CreateAPIView
from .serializer import UserSerializer,MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from userdata.models import AppUsers
from blogs.models import *

class UserRegistration(CreateAPIView):
    queryset = AppUsers.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
       
        return render(request, 'users/Register.html')
    
    def post(self, request, *args, **kwargs):
      
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
          
            if request.data.get('password') == request.data.get('password2'):
                password = make_password(request.data.get('password'))
                serializer.save(password=password) 
             
                return render(request, 'users/Login.html')
            else:
                error_messages = {'password': ['Passwords do not match.']}
                return render(request, 'users/Register.html', {'errors': error_messages})
        else:
            error_messages = serializer.errors
            return render(request, 'users/Register.html', {'errors': error_messages})
        
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




class ListUserview(ListAPIView):
    http_method_names = ['get', 'delete'] 
    def get(self, request, *args, **kwargs):
        context = {
            'users': AppUsers.objects.filter(is_superuser=False).order_by('-id')
        }
        return render(request, 'users/AdminUserList.html', context)
    
    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('userId')
       
        try:
            user = AppUsers.objects.get(id=user_id)
        
            user.delete()
            return Response({'message': 'User deleted successfully'}, status=204)
        except AppUsers.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)





def dashboard(request):
        return render(request, 'users/dashboard.html')

def LoginView(request):
        return render(request, 'users/Login.html')
def AdminBlog(request):
        context = {
             'blogs': blogdata.objects.all()
        }
        print(context,"got datacxzzx")
        return render(request, 'users/AdminBlog.html' , context)
       


