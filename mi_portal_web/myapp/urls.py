from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home',),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portafolio/', views.portafolio, name='portafolio'),
     path('testimonial/', views.testimonail, name='testimonail'),
    
]