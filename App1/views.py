
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from App1.models import Mozo, Cocinero, LavaPlatos
from App1.forms import MozoFormulario,CocineroFormulario,LavaplatosFormulario

# Create your views here.

def mozo(request):
    mozo= Mozo(nombre="Juan", apellido="Rossi", antiguedad="2020-3-11" , fechaDeNacimiento="1997-9-17" )
    mozo.save()
    documento_texto = f">Mozo: {mozo.nombre} Apellido: {mozo.apellido} Antiguedad: {mozo.antiguedad} fechaDeNacimiento: {mozo.fecha_de_nacimiento}"

    return HttpResponse(documento_texto)

def cocinero(request):
    cocinero= Cocinero(nombre="Juan3", apellido="Rossi2", antiguedad="2020-3-11" , fechaDeNacimiento="1997-9-17" )
    cocinero.save()
    documento_texto = f">Cocinero: {cocinero.nombre} Apellido: {cocinero.apellido} Antiguedad: {cocinero.antiguedad} fechaDeNacimiento: {cocinero.fecha_de_nacimiento}"

    return HttpResponse(documento_texto)

def lavaplato(request):
    lavaplatos= LavaPlatos(nombre="Juan2", apellido="Rossi3", antiguedad="2020-3-11" , fechaDeNacimiento="1997-9-17" )
    lavaplatos.save()
    documento_texto = f">Lavaplatos: {lavaplatos.nombre} Apellido: {lavaplatos.apellido} Antiguedad: {lavaplatos.antiguedad} fechaDeNacimiento: {lavaplatos.fecha_de_nacimiento}"

    return HttpResponse(documento_texto)

def inicio(request):
    return render(request,"App1/inicio.html")

def mozos (request):
    if request.method == 'POST':

        miFormulario = MozoFormulario(request.POST)

        print(miFormulario)
        
        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            mozo = Mozo (nombre=informacion['nombre'], apellido=informacion['apellido'],antiguedad=informacion['antiguedad'], fecha_de_nacimiento=informacion['fechaDeNacimiento'])
            mozo.save()
            return render(request, "App1/inicio.html") #a donde vuelve?
    else:
        miFormulario= MozoFormulario() #Formulario vacio
    return render(request,"App1/mozos.html", {"miFormulario":miFormulario})

def cocineros (request):
    if request.method == 'POST':

        miFormulario = CocineroFormulario(request.POST)

        print(miFormulario)
        
        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            cocinero = Cocinero (nombre=informacion['nombre'], apellido=informacion['apellido'],antiguedad=informacion['antiguedad'], fecha_de_nacimiento=informacion['fechaDeNacimiento'])
            cocinero.save()
            return render(request, "App1/inicio.html") #a donde vuelve?
    else:
        miFormulario= CocineroFormulario() #Formulario vacio
    return render(request,"App1/cocineros.html", {"miFormulario":miFormulario})

def lavaplatos (request):
    if request.method == 'POST':

        miFormulario = LavaplatosFormulario(request.POST)

        print(miFormulario)
        
        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            lavaplatos = LavaPlatos (nombre=informacion['nombre'], apellido=informacion['apellido'],antiguedad=informacion['antiguedad'], fechaDeNacimiento=informacion['fechaDeNacimiento'])
            lavaplatos.save()
            return render(request, "App1/inicio.html") #a donde vuelve?
    else:
        miFormulario= LavaplatosFormulario() #Formulario vacio
    return render(request,"App1/lavaplatos.html", {"miFormulario":miFormulario})

def buscar(request):
    if request.GET["apellido"]:

        apellido = request.GET['apellido']
        nombre = Mozo.objects.filter(apellido__icontains=apellido)

        return render (request, "App1/inicio.html",{"mozo":nombre, "apellido":apellido})
    else:

        respuesta = "No entraste datos"
        return HttpResponse(respuesta) #no se usa esta def

def busquedaMozos(request):
    return render (request, "App1/busquedaMozos.html")

def buscarA(request):
    if request.GET["apellido"]:
        apellido= request.GET["apellido"]
        mozo=Mozo.objects.filter(apellido=apellido)
        return render (request,"App1/resultadoBusqueda.html",{"mozo":mozo})
    else:
        return render(request,"App1/busquedaMozos.html",{"error":"No se ingreso apellido"})







