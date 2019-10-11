from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'supplyApp/index.html')


def logIn(request):

    return render(request, 'supplyApp/login.html')


def dashboard(request):
    return render(request, 'supplyApp/dashboard.html')


def edit(request):
    return render(request, 'supplyApp/edit.html')


def logOut(request):
    return render(request, 'supplyApp/index.html')