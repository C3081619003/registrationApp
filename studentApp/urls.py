from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),  # Updated this line
    path('module/', views.module, name='module'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
]