from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .decorators import groups_only

# Create your views here.
from .models import *
from .forms import CreateUserForm


def privacyPolicy(request):

    context = {}

    return render(request, 'accounts/privacyPolicy.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):

    context = {}

    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def contactUs(request):
    context = {}
    return render(request, 'accounts/contactUs.html', context)


@groups_only('StaffAdmin')
def staff_home(request):
    context = {}
    return render(request, 'accounts/staffHome.html', context)


@groups_only('StaffAdmin')
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            newuser = form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            request.POST = request.POST.copy()
            request.POST['student'] = newuser
            return redirect('signUpClass')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)
