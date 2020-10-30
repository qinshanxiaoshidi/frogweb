from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def change(request):
    return render(request, 'change.html')


def register(request):
    return render(request, 'register.html')


def Journalism(request):
    return render(request, 'Journalism.html')