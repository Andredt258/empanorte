from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SolicitudMantenimientoForm
from .models import SolicitudMantenimiento

def solicitarman(request):
    return render(request, 'solicitarman.html', {})

@login_required
def dashboard(request):
    if request.method == "GET":
        if SolicitudMantenimiento.objects.all().exists():
            solicitudes = SolicitudMantenimiento.objects.all()
            return render(request, 'dashboard.html', {'solicitudes': solicitudes})

    if request.method == 'POST':
        form = SolicitudMantenimientoForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario = request.user
            solicitud.save()
            return redirect('dashboard')
    else:
        form = SolicitudMantenimientoForm()


def missolicitudes(request):
    if request.method ==  "GET":
        if SolicitudMantenimiento.objects.all().exists():
            if request.user:
                solicitudes = SolicitudMantenimiento.objects.filter(usuario=request.user.id)
            else:
                solicitudes = SolicitudMantenimiento.objects.all()
            
            
            return render(request, 'missolicitudes.html', {'solicitudes': solicitudes})
    if request.method == 'POST':
        form = SolicitudMantenimientoForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario = request.user
            solicitud.save()
            return redirect('missolicitudes')
    else:
        form = SolicitudMantenimientoForm()
        


def mis_solicitudes(request):
    solicitudes = SolicitudMantenimiento.objects.all().order_by('fecha_creacion')
    return render(request, 'missolicitudes.html', {'solicitudes': solicitudes})


def dashboar_d(request):
    solicitudes = SolicitudMantenimiento.objects.all().order_by('fecha_creacion')
    return render(request, 'dashboard.html', {'solicitudes': solicitudes})


    

def crearusuario(request) :
    return render(request, 'crearusuario.html' , {})