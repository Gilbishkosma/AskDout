from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name='homepage'),
    path('question/',views.QuestionListView.as_view(),name='question_list'),
    path('new/',views.QuestionCreateView.as_view(),name='question_new'),
    path('<int:pk>/',views.QuestionDetailView,name="question_detail"),
    path('<int:pk>/edit/',views.QuestionUpdateView.as_view(),name="question_edit"),
    path('<int:pk>/delete/',views.QuestionDeleteView.as_view(),name="question_delete"),
    path('update/<int:pk>',views.ProfileUpdate.as_view(),name='profile_update'),
    path('profile/<int:pk>/',views.ProfileDetail.as_view(),name='profile_detail')
    
]