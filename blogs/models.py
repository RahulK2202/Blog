from django.db import models
from userdata.models import AppUsers

# Create your models here.
class blogdata(models.Model):
    image=models.ImageField(upload_to="post_img/",null=True,blank=True)
    title=models.CharField(max_length=100,null=True)
    description=models.TextField(blank=True)
    date=models.DateTimeField(auto_now_add=True)
    like_count=models.PositiveIntegerField(default=0)
    comment_count=models.PositiveIntegerField(default=0)
    user=models.ForeignKey(AppUsers,on_delete=models.CASCADE,blank=True)

    def __str__(self):
       return self.title

class Comments(models.Model):
    comment=models.TextField(blank=True)
    post=models.ForeignKey(blogdata,on_delete=models.CASCADE,blank=True)
    user = models.ForeignKey(AppUsers, on_delete=models.CASCADE,null=True) 

    class Meta:
       verbose_name='Comment'
    
    def __str__(self):
       return self.comment
    
class Like(models.Model):
   post=models.ForeignKey(blogdata,on_delete=models.CASCADE,null=True)
   user=models.ForeignKey(AppUsers,on_delete=models.CASCADE,null=True)
   liked = models.BooleanField(default=False)

   class Meta:
      unique_together=["post","user"]

   def __str__(self) -> str:
      return f"{self.user} liked on {self.post}"
