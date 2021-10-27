from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html',context)

def register(request):
    context = {}
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email  = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']

        if password == confirm_password:
            #if User.objects.filter(username=username).exist():
                #messages.error(request,'Username already exist')
                #return redirect('register')
            #else:
                #if User.objects.filter(email=email).exist():
                    #messages.error(request,'Email already exist')
                    #return redirect('register')
                #else:
            user = User.objects.create_user(first_name = firstname, last_name = lastname, email=email, username = username,password = password)
            auth.login(request, user)
            messages.success(request, 'you are now logged in ')
            return redirect('dashboard')
            user.save()
            messages.success(request,'you are registered successfully')
            return redirect('login')
        else:
            messages.error(request,'password do not match')
            return redirect('register')



        
    else:
        return render(request,'accounts/register.html',context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'you are successfully logged out')
        return redirect('index')
    context = {}
    return render(request,'accounts/logout.html',context)

def reset(request):
    context = {}
    return render(request,'accounts/reset.html',context)

def dashboard(request):
    context = {}
    return render(request,'accounts/dashboard.html',context)