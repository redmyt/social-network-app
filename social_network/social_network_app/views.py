from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from .models import Profile, Message, FriendsRecord
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


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
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data['username']
            created_user = User.objects.get(username=username)
            user_profile = Profile(user=created_user,
                                   phone=profile_form.cleaned_data['phone'])
            user_profile.save()
            login(request, created_user)
            return redirect(reverse('user_page'))

        errors = []
        errors.append(user_form.errors.items())
        errors.append(profile_form.errors.items())
        return render(request, 'start.html', errors)


@csrf_exempt
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(reverse('user_page'))

    return render(request, 'start.html')


@csrf_exempt
def logout_view(request):
    logout(request)
    return render(request, 'start.html')


@login_required(login_url='start_page')
def friends_view(request):
    user_profile = Profile.objects.get(user=request.user)
    records = FriendsRecord.objects.all().filter(Q(first_friend=user_profile) |
                                                 Q(second_friend=user_profile))

    friends = []

    for record in records:
        if record.first_friend != user_profile:
            friends.append(record.first_friend)
        elif record.second_friend != user_profile:
            friends.append(record.second_friend)

    return render(request, 'friends.html', friends)


@csrf_exempt
@login_required(login_url='start_page')
def messages_view(request):
    if request.method == 'GET':
        user_profile = Profile.objects.get(user=request.user)
        messages = Message.objects.all().filter(Q(sender=user_profile) |
                                                Q(receiver=user_profile))
        return render(request, 'messindex.html', {'messages': messages})

    elif request.method == 'POST':
        try:
            sender = request.user.profile
            receiver_username = request.POST.get('receiver')
            receiver = User.objects.get(username=receiver_username).profile
            message_body = request.POST.get('message_body')
            date = request.POST.get('date')

            message = Message(sender=sender, receiver=receiver,
                              message_body=message_body, date=date)
            message.save()
        except Exception as err:
            return render(request, 'messindex.html', {'err': err})
        finally:
            return render(request, 'messindex.html')


def emojisPage_view(request):
    return render(request, 'emojisPage.html')


def emojis2_view(request):
    return render(request, 'emojis.html')
