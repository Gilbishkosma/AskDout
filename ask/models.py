from django.db import models
from django.urls import reverse
from django.conf import settings


class Question(models.Model):
     title = models.CharField(max_length=100)
     body = models.TextField()
     date = models.DateTimeField(auto_now_add=True)
     image = models.ImageField(upload_to = 'img/',null=True,blank=True)
     person = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
     def __str__(self):
     	 return self.title
     def get_absolute_url(self):
      	return reverse('question_detail',args=[str(self.id)])


class Comment(models.Model):
     question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='comments')
     comment = models.CharField(max_length=100)
     person = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
     
     def __str__(self):
     	 return self.comment
     


class Profile(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profileuser')
     image = models.ImageField(upload_to = 'img/',null=True,blank=True)
     Bio = models.TextField(null=True,blank=True);
     Education_qualification = models.TextField(null=True,blank=True)
     age = models.PositiveIntegerField(default=0)
     email = models.EmailField(max_length=200)
     def __str__(self):
          return '{} yo '.format(self.Bio);
     def get_absolute_url(self):
          return reverse('profile_detail',args=[str(self.id)])
