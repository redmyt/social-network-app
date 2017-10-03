from django.shortcuts import render


def start_page_view(request):
    return render(request, 'base.html')

def login_view(request):
    return render(request, 'login.html')

def regester_view(request):
    return render(request, 'regester.html')