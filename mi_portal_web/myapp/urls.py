from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home',),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portafolio/', views.portafolio, name='portafolio'),
    path('testimonial/', views.testimonail, name='testimonail_list'),
    path('testimonial/register',views.testimonio_registro, name = 'testmonial_register'),
    path('events/register/',views.event_register_view, name='event_register'),
    path('events/',views.event_list_view, name='event_list'),
    ]