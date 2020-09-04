from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
<<<<<<< HEAD
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
#     path('user:author/<int:pk>/', views.AuthorView.as_view(), name='author-detail'),
=======
    path('add-story/', views.AddStoryView.as_view(), name='newStory')
>>>>>>> parent of 339b986... completed author stories
]
