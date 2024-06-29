from django.shortcuts import render, redirect, get_object_or_404
from .models import Turno
# Create your views here.


def index(request):
    return render(request, 'gestion_peluqueria/index.html')

def base(request):
    return render(request, 'gestion_peluqueria/base.html')


def home(request):
    return render(request, 'gestion_peluqueria/home.html')

def servicios(request):
    return render(request, 'gestion_peluqueria/servicios.html')

def contacto(request):
    return render(request, 'gestion_peluqueria/contacto.html')

def sucursales(request):
    return render(request, 'gestion_peluqueria/sucursales.html')

def tienda(request):
    return render(request, 'gestion_peluqueria/tienda.html')

def nosotros(request):
    return render(request, 'gestion_peluqueria/nosotros.html')

# Codigo ClassTurno

def gestionTurno(request):
    turnosListados = Turno.objects.all()
    return render(request, 'gestion_peluqueria/gestionTurno.html', {'turnos': turnosListados})

def registrarTurno(request):
    nombre=request.POST['nombre']
    fecha=request.POST['fecha']
    hora=request.POST['hora']
    
    
    turno = Turno(
        nombre=nombre, fecha=fecha, hora=hora)
    turno.save()
    
    return redirect('/gestionTurno/') 

def eliminarTurno(request, id):
    eliminarturno = get_object_or_404(Turno, id=id)
    eliminarturno.delete()
    
    return redirect('/gestionTurno/')

def edicionTurno(request, id):
    turno = get_object_or_404(Turno, id=id)
    return render(request, 'gestion_peluqueria/edicionTurno.html', {"turno": turno})

def editarTurno(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    fecha=request.POST['fecha']
    hora=request.POST['hora']
    
   
    turno = Turno.objects.get(id=id)
    turno.nombre = nombre
    turno.fecha = fecha
    turno.hora = hora
    turno.save()
    
    return redirect('/gestionTurno/') 

