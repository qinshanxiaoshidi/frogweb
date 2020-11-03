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

def gyzf(request):
    return render(request, 'gyzf.html')

def zwz(request):
    return render(request, 'zwz.html')

def jlb(request):
    return render(request, 'jlb.html')

def mrt(request):
    return render(request, 'mrt.html')

def luntan(request):
    return render(request, 'luntan.html')

def develop(request):
    return render(request, 'develop.html')