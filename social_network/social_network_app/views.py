from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import *
from .models import Profile
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
        if user_form.is_valid() and profile_form.is_valid():
            user = User(**user_form.cleaned_data)
            user.save()
            created_user = User.objects.get(username=user_form.cleaned_data['username'])
            user_profile = Profile(user=created_user,
                                   phone=profile_form.cleaned_data['phone'])
            user_profile.save()


def friends_view(request):
    return render(request, 'friends.html')

def emojisPage_view(request):
    return render(request, 'emojisPage.html')

def emojis2_view(request):
    return render(request, 'emojis.html')
