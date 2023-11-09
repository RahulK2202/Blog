from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from .models import blogdata
from rest_framework.generics import UpdateAPIView,ListAPIView,CreateAPIView,DestroyAPIView,ListCreateAPIView
from .serializer import *
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.decorators import api_view



from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class AdminAddBlogs(CreateAPIView):
    queryset = blogdata.objects.all()
    serializer_class = AddPostSerializer
    template_name = 'users/AdminAddBlog.html'

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
       
        try:
            user = AppUsers.objects.get(id=user_id)
            image = request.data.get('image')
            title = request.data.get('title')
            description = request.data.get('description')
         

            if user and image and title and description:
                blog = blogdata.objects.create(
                    image=image,
                    description=description,
                    title=title,
                    user=user
                )

                return redirect(reverse('adminblog'))
            else:
                return Response({'message': 'Missing required data'})
        except AppUsers.DoesNotExist:
            return Response({'message': 'User not found'})
    

def DeleteBlog(request, blogId):
    blog = get_object_or_404(blogdata, id=blogId)
    blog.delete()
    return redirect('adminblog')



class UpdateBlogPost(APIView):
  
    def get(self, request, blogId):
        try:
         
            blog = blogdata.objects.get(id=blogId)
       
            
            context = {'blog_data': blog}
            return render(request, 'users/AdminEditBlog.html', context)
        except blogdata.DoesNotExist:
            raise Http404
        
    def post(self, request, blogId):
        blog = blogdata.objects.get(id=blogId)
   
       
        serializer = BlogdataSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse('adminblog'))
        else:
            context = {'blog_data': blog, 'errors': serializer.errors}
            return render(request, 'users/AdminEditBlog.html', context)



def AddBlog(request):
        
        return render(request, 'users/AdminAddBlog.html')

def UserHome(request):

        
      
        context = {
             'blogs': blogdata.objects.all()
        }
   
        return render(request, 'users/UserBlogList.html' , context)

@api_view(['POST'])
def add_comment(request):
   


    user_id = request.data.get('userid')
  
    post_id = request.data.get('post')
    comment_text = request.data.get('comment')
  

  

    serializer = CommentSerializer(data={
        'user': user_id,
        'post': post_id,
        'comment': comment_text,
    })

    if serializer.is_valid():
        serializer.save()
    
        return redirect('home')
    return Response(serializer.errors)
    

class GetComments(APIView):
    def get(self, request, post_id):
        try:
      
       
            blog = get_object_or_404(blogdata, pk=post_id)

       
            blogs = blogdata.objects.all()

      
            comments = Comments.objects.filter(post=post_id)
      
            context = {
                'comments': comments,
                'blogs': blogs,  
                'error': None,
            }
         
            
            return render(request, 'users/UserBlogList.html', context)
        
        except blogdata.DoesNotExist:
            error = 'Blog not found'
            context = {
                'comments': [],
                'blogs': blogs,  
                'error': error,
            }
            
  
            return render(request, 'users/UserBlogList.html', context)
        


def LikeorDislike(request, post_id):
    user_id = request.POST.get('user_id')
    values = request.POST.get('like_value')
 
    
 

    try:
        
        user = AppUsers.objects.get(id=user_id)
        post = get_object_or_404(blogdata, pk=post_id)

        try:
            like = Like.objects.get(user=user, post=post)

            if values == "1":
                like.liked = False
                like.delete()
            else:
                like.liked = True
                like.save()
        except Like.DoesNotExist:
     
            if values == "0":
                Like.objects.create(user=user, post=post, liked=True)

        liked_posts = [like.post.id for like in Like.objects.filter(user=user, liked=True)]
        blogs = blogdata.objects.all()

        context = {'liked_posts': liked_posts, 'blogs': blogs}
        return render(request, 'users/UserBlogList.html', context)
    except AppUsers.DoesNotExist:
        return redirect('home')
    



class UserLogoutAPIView(GenericAPIView):
   

    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            print("reacheddddd")
            refresh_token = request.data["refresh"]
            print(refresh_token,"refresh tokennnnnnnnnnnnn")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response()
        except Exception as e:
            return Response()

