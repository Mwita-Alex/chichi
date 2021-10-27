from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request,'pages/home.html',context)


def about(request):
    context = {}
    return render(request,'pages/about.html',context)

def team(request):
    context = {}
    return render(request,'pages/team.html',context)

def home2(request):
    context = {}
    return render(request,'pages/home2.html',context)
