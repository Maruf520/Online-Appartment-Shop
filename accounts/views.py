from django.shortcuts import render, redirect
from . import views

def login(request):
      if request.method == 'post':
      #login User

       return    
      else:
        return  render(request, 'accounts/login.html' )


       

def register(request):
      if request.method == 'post':
      #Register User
      
            print("Submitted Reg")
            return redirect('register')
      else:
        return render(request, 'accounts/register.html')


    

def logout(request):
    return render (request, 'accounts/logout.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')    