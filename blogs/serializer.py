from .models import *
from userdata.models import AppUsers
from rest_framework import serializers



class UserdataSerializer(serializers.ModelSerializer):
    class Meta:
        model=AppUsers
        fields= '__all__'

class AddPostSerializer(serializers.ModelSerializer):

    user =  UserdataSerializer()
    # user = serializers.PrimaryKeyRelatedField(queryset=AppUsers.objects.all())
    class Meta:
        model = blogdata
        fields = ["image","title","description","user"]

class BlogdataSerializer(serializers.ModelSerializer):
    class Meta:
        model=blogdata
        fields= '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    user = UserdataSerializer()

    class Meta:
        model = Comments
        fields = '__all__'



# class CommentSerializer(serializers.ModelSerializer):
#     user=serializers.SerializerMethodField()
#     class Meta:
#         model=Comments
#         fields='__all__'
#         extra_kwargs={
#             'user':{'write_only':True}
#         }
#     def get_userdetails(self,obj):
#         userdetails = {}
#         userdetails.update(username=UserSerializer(obj.user).data.get('username'))
#         userdetails.update(pic=UserSerializer(obj.user).data.get('pic'))
#         return userdetails





