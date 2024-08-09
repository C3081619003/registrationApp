from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def home(request): 

  return render(request, 'studentApp/home.html')


def about(request): 

  return render(request, 'studentApp/about.html')


def contact(request): 

  return render(request, 'studentApp/contact.html')

def modules(request): 

  return render(request, 'studentApp/modules.html')