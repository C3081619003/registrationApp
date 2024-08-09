from . import views 
from django.urls import path, include 


#app_name = 'studentApp' 

urlpatterns = [ 

    path('', views.home, name = 'home'), 
    path('about/', views.about, name = 'about'), 
    path('contact/', views.contact, name = 'contact'), 
    path('modules/', views.modules, name = 'modules'), 
]