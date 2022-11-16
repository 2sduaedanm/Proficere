from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class CreateUserForm(UserCreationForm):
    is_student = forms.BooleanField(initial=True, required=False)
    is_instructor = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2', 'is_student', 'is_instructor']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.EmailField(required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.EmailField(required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UpdateUserProfileForm(forms.ModelForm):
    birthdate = forms.DateField()
    userphoto = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control-file'}))

    class Meta:
        model = UserProfile
        fields = ['birthdate', 'userphoto']
