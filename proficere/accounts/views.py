from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .decorators import groups_only

# Create your views here.
from .models import *
from .forms import CreateUserForm, UpdateUserForm, UpdateUserProfileForm


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
            print('Check request' + str(request.POST['is_student']))
            print('Check form1' + str(form.cleaned_data.get('is_student')))
            print('Check form2' + str(form.cleaned_data['is_student']))
            newuser = form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            if request.POST['is_student']:
                print('I am inside')
                student_group = Group.objects.get(name="Student")
                newuser.groups.add(student_group)
                print(student_group)
            if form.cleaned_data.get('is_instructor'):
                instructor_group = Group.objects.get(name='Instructor')
                newuser.groups.add(instructor_group)
            return redirect('userprofile')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@groups_only('StaffAdmin')
def userprofile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        userprofile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.accounts.userprofile)

        if user_form.is_valid() and userprofile_form.is_valid():
            user_form.save()
            userprofile_form.save()
            messages.success(
                request, 'Your user profile is updated successfully')
            return redirect(to='accounts-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        userprofile_form = UpdateUserProfileForm(
            instance=request.accounts.userprofile)

    return render(request, 'accounts/userprofile.html', {'user_form': user_form, 'userprofile_form': userprofile_form})


@login_required(login_url='login')
def signUpClass(request):
    context = {}
    return render(request, 'accounts/signUpClass.html', context)
