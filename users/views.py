from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from. import models
# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        print("i am here")
        if password==confirm_password:


            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
            else:
                print("i am here again**************")
                models.register_model(first_name,last_name,username,email,password)
                return redirect(login)
        else:
             messages.info(request,'password not matched...')
        return redirect(register)
    else:
      return render(request,'users/register.html')


"""
def login(request):
    if request.method=='POST':
        username=request.POST('username')
        password=request.POST('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:

        return render(request,"users/login.html")

"""
def login(request):
    if request.session.__contains__('username'):
        return render(request, 'index.html', {})
    if request.method == 'POST':
        username = request.POST.get('username', False)
        pwd = request.POST.get('password', False)

        username = models.login_model(username, pwd)
        print(username)

        if username != None:
            request.session['username'] = username
          #  request.session['phone']= phone_no

          #  models.is_active(username, phone_no)
            return render(request, 'index.html')
    else:
        return render(request, 'users/login.html', {})


    return render(request, 'users/login.html', {})



def logout(request):
    auth.logout(request)
    return redirect('index')


