from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .models import Question,Comment,Profile
from .forms import Commentform
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView

# Create your views here.


class HomePageView(TemplateView):
	template_name = 'home.html'

class QuestionListView(LoginRequiredMixin,ListView):
   model = Question
   template_name = 'question_list.html'
   login_url = 'login'
   def get_queryset(self):
        if self.request.method == 'GET':
          search = self.request.GET.get('search')
        if search == None:
           search = '' 
        return Question.objects.all().filter(title__icontains = search)

def QuestionDetailView(request,pk):
   question = Question.objects.get(id=pk);
   template_name = 'question_detail.html'
   if request.method == 'POST':
       form = Commentform(request.POST)
       if form.is_valid():
          new_comment = form.save(commit = False)
          new_comment.question = question
          new_comment.person = request.user
          new_comment.save()
          return redirect('question_detail',pk=pk)
   else:
      form = Commentform()
   return render(request,'question_detail.html',{'form':form,'question':question})

class QuestionUpdateView(LoginRequiredMixin,UpdateView):
      model = Question
      fields = ['title','body','image']
      template_name = 'question_edit.html'
      login_url = 'login'
      def dispatch(self,request,*args,**kwargs):  #dispatch works
      	  handler = super(QuestionUpdateView,self).dispatch(request,*args,**kwargs) #handler will store the current data
      	  if self.object.person != request.user: #object refers to current Question
      	  	  return redirect('question_list') 
      	  return handler 

class QuestionDeleteView(LoginRequiredMixin,DeleteView):
     model = Question
     template_name = 'question_delete.html'
     success_url = reverse_lazy('question_list')
     login_url = 'login'
     def dispatch(self,request,*args,**kwargs):  #dispatch works
      	  handler = super(QuestionDeleteView,self).dispatch(request,*args,**kwargs) #handler will store the current data
      	  if self.object.person != request.user: #object refers to current question
      	  	  return redirect('question_list') 
      	  return handler 

class QuestionCreateView(LoginRequiredMixin,CreateView):
   model = Question
   template_name = 'question_new.html'
   fields = ['title','body']
   login_url = 'login'

   def form_valid(self,form): #if form is valid
     form.instance.person = self.request.user
     return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin,UpdateView):
      model = Profile
      fields = ['image','Bio','Education_qualification','age',]
      template_name = 'profile_update.html'
      login_url = 'login'
      def dispatch(self,request,*args,**kwargs):  #dispatch works
          handler = super(ProfileUpdate,self).dispatch(request,*args,**kwargs) #handler will store the current data
          if self.object.user != request.user: #object refers to current Question
              return redirect('question_list') 
          return handler

class ProfileDetail(LoginRequiredMixin,DetailView):
      model = Profile
      template_name = 'profile_detail.html'

