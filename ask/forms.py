from django import forms
from .models import Comment


class Commentform(forms.ModelForm):
	 class Meta:
	 	model = Comment
	 	fields = ['comment']
	 	widgets = {
              'comment':forms.Textarea(attrs={'class':'form-control',"rows":5,"cols":20})
           }