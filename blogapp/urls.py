from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'blogs'


urlpatterns=[
    path('home/', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('post/', TemplateView.as_view(template_name='post.html'), name='post'),
]