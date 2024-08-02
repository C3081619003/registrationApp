from . import views 
from django.urls import path, include 


#app_name = 'studentApp' 

urlpatterns = [ 

    path('', views.home, name = 'home'), 
]