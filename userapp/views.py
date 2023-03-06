from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import *
from django.views import View

class LoginView(View):
    def post(self,request):
            user = authenticate(username=request.POST.get('username'),
                                password=request.POST.get('password'))
            if user is None:
                return redirect('/')
            login(request, user)
            return redirect('/main/')
    def get(self, request):
        return render(request, 'page-user-login.html')

def logoutview(request):
    logout(request)
    return redirect('/')

class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')