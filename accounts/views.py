from django.shortcuts import render, redirect
from . import views
from django.contrib import messages, auth
from django.contrib.auth.models import User
def login(request):
      if request.method == 'POST':
      #login User
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user is not None:
               auth.login( request, user ) 
               messages.error(request, 'You are logged in ')  
               return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials')    
                return redirect( 'login') 

         
      else:
            return  render(request, 'accounts/login.html' )


       

def register(request):
      if request.method == 'POST':
      #get values
          first_name = request.POST['first_name']
          last_name = request.POST['last_name']
          username = request.POST['username']
          email = request.POST['email']
          password = request.POST['password']
          password2 = request.POST['password2']
          
          if password == password2:
          
                if User.objects.filter(username=username).exists():
                   messages.error(request, 'Username is taken.')
                   return redirect('register')
                else:
                      if User.objects.filter(email=email).exists():
                          messages.error(request, 'Email is taken.')
                          return redirect('register')
                      else:
                              user =  User.objects.create_user( username = username, first_name = first_name, last_name = last_name, email = email, password = password ) 
                              user.save()
                              messages.error(request, "you are registered now,") 
                              return redirect('login')


          else:
                messages.error(request,'password do not match')
                return redirect('register')

      #Register User
          messages.error(request, 'Testing error messages')
          return redirect('register')
      else:
          return render(request, 'accounts/register.html')


    

def logout(request):
    return render (request, 'accounts/logout.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')    