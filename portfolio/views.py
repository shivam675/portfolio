from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Project, contact, Certificate
from blog.models import Blog
from .forms import ContactForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    blogs = Blog.objects.order_by("-date")[:3]
    return render(request, 'updated/home_page.html', {'blogs':blogs})

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'portfolio/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'portfolio/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'portfolio/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'portfolio/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'portfolio/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def gsoc2021(request):
    return render(request, 'portfolio/gsoc_python_challenge.html')


def roboticsAcademychallenge(request):
    return render(request, 'portfolio/roboticsAcademychallenge.html')


def contact_me(request):
    if request.method == 'POST':
        conf = ContactForm(request.POST or None)
        if conf.is_valid():
            f_name = request.POST.get('first_name')
            l_name = request.POST.get('last_name')
            email = request.POST.get('email_adress')
            content = request.POST.get('message')
            obj = contact.objects.create(first_name = f_name, last_name = l_name, email_adress = email, message = content)
            obj.save()
            return render(request,'updated/contact.html', { 'success' :'Form submitted successfully !!' })

        else:
            return render(request, 'updated/contact.html')
    else:
        conf = ContactForm()
        return render(request, 'updated/contact.html', {'comment_form':conf})


def base(request):
    return render(request, 'updated/base.html')

def major_projects(request):
    projects = Project.objects.order_by('-date_of_completion')
    return render(request, 'updated/projects.html',  {'projects':projects})


def certification(request):
    Certificates = Certificate.objects.order_by('-priority_number')
    # print(Certificates)
    return render(request, 'updated/certifications.html',  {'Certificates':Certificates})
