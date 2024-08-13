from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm


def home(request):
    return render(request, 'studentApp/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = UserRegistrationForm()
    return render(request, 'studentApp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('module')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'studentApp/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')



@login_required
def module(request):
    courses = [
        {
            'name': 'Computing',
            'code': '1111',
            'level': 'Postgrad',
            'duration': '1 year/2 years',
            'modules': [
                {'id': 1, 'name': 'Cloud Computing'},
                {'id': 2, 'name': 'Database Management'}
            ]
        },
        {
            'name': 'Engineering',
            'code': '1112',
            'level': 'Undergrad',
            'duration': '3 years',
            'modules': [
                {'id': 3, 'name': 'Electrical Engineering'},
                {'id': 4, 'name': 'Robotics'}
            ]
        },
        {
            'name': 'Biomedicine and Health Science',
            'code': '1113',
            'level': 'Undergrad',
            'duration': '4 years',
            'modules': [
                {'id': 5, 'name': 'Human Anatomy'},
                {'id': 6, 'name': 'Epigenetics'}
            ]
        },
        {
            'name': 'Chemistry',
            'code': '1114',
            'level': 'Postgrad',
            'duration': '2 year',
            'modules': [
                {'id': 7, 'name': 'Principles Of Chemistry'},
                {'id': 8, 'name': 'Organic and Biosynthetic Chemistry'}
            ]
        },
        {
            'name': 'Business Studies',
            'code': '1115',
            'level': 'Undergrad',
            'duration': '3 years',
            'modules': [
                {'id': 9, 'name': 'Market Management'},
                {'id': 10, 'name': 'Organisational Structures'}
            ]
        },
        {
            'name': 'Law',
            'code': '1116',
            'level': 'Undergrad',
            'duration': '4/5 years',
            'modules': [
                {'id': 11, 'name': 'Criminal Law'},
                {'id': 12, 'name': 'Human Rights and Justice'}
            ]
        }
    ]

    
    return render(request, 'studentApp/module.html', {'courses': courses})

def about(request):
    return render(request, 'studentApp/about.html')

def contact(request):
    return render(request, 'studentApp/contact.html')

@login_required
def module(request):
    return render(request, 'studentApp/module.html')