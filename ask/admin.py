from django.contrib import admin
from .models import Question,Comment,Profile
# Register your models here.

class CommentInline(admin.TabularInline):
	 model = Comment

class QuestionAdmin(admin.ModelAdmin):
	inlines = [CommentInline,]



admin.site.register(Question,QuestionAdmin)
admin.site.register(Comment)
admin.site.register(Profile)
