from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import MemberForm
from django.http import HttpResponse,HttpResponseRedirect
from .models import Member

#creating pdf files
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
#from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import os
from reportlab.lib.units import mm

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
            if User.objects.filter(username=username).count():
                messages.error(request,'Username already exist')
                return redirect('register')
            #else:
                #if User.objects.filter(email=email).exist():
                    #messages.error(request,'Email already exist')
                    #return redirect('register')
            else:
                user = User.objects.create_user(first_name = firstname, last_name = lastname, email=email, username = username,password = password)
                auth.login(request, user)
                messages.success(request, 'you are now logged in ')
                user.save()
                return redirect('dashboard')
            #messages.success(request,'you are registered successfully')
            #return redirect('login')
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
    if request.method == 'POST':
         form = MemberForm(request.POST,request.FILES)
         if form.is_valid():
             newmember = form.save(commit=False)
             newmember.user = request.user
             newmember.save()
             return redirect('downloadpdfform')
         else:
             return render(request,'accounts/dashboard.html',context)
    else:
        memberform = MemberForm()
        context = {'form': memberform}
        if Member.objects.filter(user=request.user).count():
             return redirect('downloadpdfform')
        else:
             return render(request,'accounts/dashboard.html',context)

            
        
       


    #if request.method == 'GET':
       # memberdetails = Member.objects.filter(user=request.user, graduation_year__isnull=False) 
        #if memberdetails is None:   
            #memberform = MemberForm()
            #context = {'form': memberform}
            #return render(request,'accounts/dashboard.html',context)
        #else:
             #return redirect('downloadpdfform')



    
    #else:
        
       # if memberdetails is None:   
           # memberform = MemberForm()
           # context = {'form': memberform}
            #return render(request,'accounts/dashboard.html',context)
        #else:
            #memberdetails = Member.objects.filter(user=request.user)
            

    
def downloadpdfform(request):
  memberdetails = Member.objects.filter(user=request.user)
  return render(request,'accounts/downloadpdf.html',{'details': memberdetails})


def pdfgenerator(request):
    title = "UCSPAK IDENTITY CARD"
    name = "Name: "
    university = "University: "
    admission = "Admission: "
    graduation = "Graduation: "
    phone = "Phone: "
    buf = io.BytesIO()
    c = canvas.Canvas(buf, bottomup=0)
    #textob = c.beginText()
    #textob.setTextOrigin(inch, inch)
    #textob.setFont("Helvetica", 14)

   #create real stuffs
   
    memberdetails = Member.objects.filter(user=request.user)
    for memberdetail in memberdetails:
    
        logoleft = root + '/media/' +  str(memberdetail.member_image)
        width = 86*mm
        height = 54*mm
        c.setPageSize((width,height))
        c.drawImage(logoleft, 5, 5, height=20*mm, width=20*mm)
        c.setFont('Helvetica',12)
        c.setFillColorRGB(0, 0,255)
        c.drawString(70, 20, title)
        c.line(71, 25, 215, 25)
        c.setFont('Courier',12)
        c.setFillColorRGB(0, 0,255)
        c.drawString(70, 40, name)
        c.setFillColorRGB(0, 0, 0)
        c.drawString(110, 40, memberdetail.student_name)
        c.setFillColorRGB(0, 0,255)
        c.drawString(70, 60, admission)
        c.setFillColorRGB(0, 0, 0)
        c.drawString(150, 60, memberdetail.admission_number)
        c.setFillColorRGB(0, 0,255)
        c.drawString(10, 80, university)
        c.setFillColorRGB(0, 0, 0)
        c.drawString(90, 80, memberdetail.university_name)
        c.setFillColorRGB(0, 0,255)
        c.drawString(10, 100, phone)
        c.setFillColorRGB(0, 0, 0)
        c.drawString(60, 100, memberdetail.phone_number)
        c.setFillColorRGB(0, 0,255)
        c.drawString(10, 120, graduation)
        c.setFillColorRGB(0, 0, 0)
        c.drawString(90, 120, memberdetail.graduation_year)
        
    #lines = []
    #for memberdetail in memberdetails:
       #  c.drawInlineImage(0,0,memberdetail.member_image)
      # lines.append(memberdetail.student_name)
      # lines.append(memberdetail.university_name)
      # lines.append(memberdetail.phone_number)
      # lines.append(memberdetail.admission_number)
      # lines.append(memberdetail.graduation_year)
      # lines.append(str(memberdetail.member_image))

    #create testing stuffs
   
    #for line in lines:
        #textob.textLine(line)

   # c.drawText(textob)
    #c.drawInlineImage(memberdetails.member_image)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True,filename='ucspak membership-card.pdf')


       
     