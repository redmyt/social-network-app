from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm 
from .models import Profile
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def user_page_view(request):
    return render(request, 'base.html')


@csrf_exempt
def start_page_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return redirect(reverse('user_page'))
        else:
            return render(request, 'start.html')

    elif request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        # print(user_form.is_valid())
        if user_form.is_valid() and profile_form.is_valid():
            # user = User(**user_form.cleaned_data)
            # user.save()
            user_form.save()
            created_user = User.objects.get(username=user_form.cleaned_data['username'])
            # user_profile = Profile(user=created_user,
                                   # phone=profile_form.cleaned_data['phone'])
            # user_profile.save()
            login(request, created_user)
            return redirect(reverse('user_page'))

@csrf_exempt
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    # print(username)
    # print(password)
    user = User.objects.get(username=username)
    # if user is not None:
        # if user.is_active:
    login(request, user)

@csrf_exempt    
def logout_view(request):
    logout(request)
    return render(request, 'start.html')

def friends_view(request):
    return render(request, 'friends.html')

@login_required
def messages_view(request):
    user = User.objects.get(pk=request.user.id)
    print(user)
    return render(request, 'messindex.html')

def emojisPage_view(request):
    return render(request, 'emojisPage.html')

def emojis2_view(request):
    return render(request, 'emojis.html')

