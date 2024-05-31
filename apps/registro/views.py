from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def solicitarman(request):
    return render(request, 'solicitarman.html', {})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {})

def missolicitudes(request):
    if request.method == 'POST':
        machine = request.POST.get('machine')
        averia = request.POST.get('averia')
        description = request.POST.get('description')
        
        # Procesa los datos como necesites. Por ejemplo, puedes guardarlos en la base de datos:
        # my_model_instance = MyModel(machine=machine, averia=averia, description=description)
        # my_model_instance.save()

        print(machine)
        print(averia)
        print(description)
        print("Datos recibidos y procesados")

        return redirect('dashboard')  # Redirige a la vista que consideres adecuada después del POST
    
    return render(request, 'missolicitudes.html')

def crearusuario(request) :
    return render(request, 'crearusuario.html' , {})