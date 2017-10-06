from django.shortcuts import render


def base_view(request):
    return render(request, 'base.html')

def start_page_view(request):
    return render(request, 'start.html')

def friends_view(request):
    return render(request, 'friends.html')
