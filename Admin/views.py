from django.contrib.auth.models import User
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from  django.contrib import messages
# Create your views here.




def admin_register(request):
    return render(request,'admin/admin_signup.html')

def admin_signup(request):
    if request.method=='POST':
        # type=request.POST['type']
        name=request.POST['Name']
        email=request.POST['Email']
        phone=request.POST['Phone']
        password=request.POST['Password']
        cpassword=request.POST['Cpassword']
        if password == cpassword:
            if Admin.objects.filter(username=email).exists():
                messages.info(request,"Username already exists")
                return HttpResponse('<script>alert("Username Exists");window.location="register"</script>')
            else:
                user=Admin.objects.create(type=type,name=name,username=email,phone=phone,password=password)
                user.save()
                print(user)
                return redirect('loginPage')
        else:
            print("Password doesnot match")
            return HttpResponse('<script>alert("Password doesnot match");window.location="register"</script>')
    else:
        return render(request,'signup_index.html')


def view_user(request):
    context= {'users':User.objects.all()}
    return render(request, 'QuesAnswers.html',context)