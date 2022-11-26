from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import *
from .decorators import *
from .models import *



@unauthendicated_user
def index(request):

    return render(request,'genz/first_page.html')

@unauthendicated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = form.cleaned_data.get('group')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context={'form':form}
    return render(request, 'genz/register.html', context)

@unauthendicated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "username or password is incorrect")
    context={}
    return render(request, 'genz/login.html', context)

@login_required(login_url='login')
def homePage(request):
    
    groups = request.user.groups.all()
    

    
    team_list = teams.objects.all().values_list('name')
    team_name =[]
    for team in team_list:
        comma_delim = ''
        r = comma_delim.join(team)
        team_name.append(r)
    numb_team = len(team_name)
    context = {
        'groups':groups,
        'teams':team_name,
        'numb_team':numb_team,
    }
    return render(request, 'genz/home.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('first-page')


def ex_form(request):

    if request.method == 'POST':
        exForm = ExpertForm(request.POST)
        if exForm.is_valid():
            exForm.save()

    context = {
        'exForm':exForm,
    }
    return render(request, 'genz/home.html', context)
