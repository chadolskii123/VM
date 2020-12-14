from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'blogs'


urlpatterns=[
    path('home/', views.PostListView.as_view(), name='home'),
    path('daily/', views.DailyListView.as_view(), name='daily'),
    path('skills/', views.SkillsListView.as_view(), name='skills'),
    path('tips/', views.TipsListView.as_view(), name='tips'),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('post/', TemplateView.as_view(template_name='post.html'), name='post'),
    path('save', views.savePost, name='save'),
    path('create', views.PostCreateView.as_view(), name='create'),
]