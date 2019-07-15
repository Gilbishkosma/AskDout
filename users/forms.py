from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

	 class Meta(UserCreationForm.Meta):
	 	  model = CustomUser
	 	  fields = ('username','email',) #i didn't provide pass cause pass is mandatory so it will include it


class CustomUserChangeForm(UserChangeForm):

	class Meta:
		 model = CustomUser
		 fields = ('username','email',) #using default Meta fields


#UserCreationForm and UserChangeForm are the inbuilt classes of django default form
#We are just extending both
#UserCreationForm are used when we sign up
#UserchangeForm are used when we change something from admin site