from django.shortcuts import render


def start_page_view(request):
    return render(request, 'base.html')

def friends_view(request):
    return render(request, 'friends.html')