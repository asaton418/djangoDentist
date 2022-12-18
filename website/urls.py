from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('service.html', views.service, name="service"),    
    path('appointment.html', views.appointment, name="appointment"),
    path('appointment2.html', views.appointment2, name="appointment2"),      
    path('price.html', views.price, name="price"),
    path('service.html', views.service, name="service"),
    path('team.html', views.team, name="team"),          
    path('testimonial.html', views.testimonial, name="testimonial"),   
]

