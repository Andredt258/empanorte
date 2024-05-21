from django.shortcuts import render



def solicitarman(request):
    return render(request,'solicitarman.html',{})

def dashboard(request):
    return render(request,'dashboard.html',{})

def missolicitudes(request):
    return render(request,'missolicitudes.html',{})

def login(request):
    return render(request,'login.html',{} )