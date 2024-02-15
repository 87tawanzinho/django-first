from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else: 
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first() # traz do banco de dados os usuarios que eu tenho

        if user: 
            return HttpResponse('Já existe um usuário com esse username')
        
        
        newUser = User.objects.create_user(username=username, email=email, password=password)
        newUser.save()
        return render(request, 'home.html')

def login(request):
   if request.method == 'GET':
        return render(request, 'login.html')
   else: 
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = authenticate(username=username, password=password)
       if user: 
           login_django(request, user)
           return redirect('home')
       else:
           return HttpResponse("Email ou senha invalidos.")
       

@login_required(login_url="/auth/login/")
def home(request):
    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect('login')
    user = request.user.username
    return render(request, 'home.html', {'username': user})

def user_logout (request): 
    logout(request)
    return redirect('login')