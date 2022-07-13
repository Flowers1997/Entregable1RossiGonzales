
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
    cocinero= Cocinero(nombre="Juan", apellido="Rossi", antiguedad="2020-3-11" , fechaDeNacimiento="1997-9-17" )
    cocinero.save()
    documento_texto = f">Cocinero: {cocinero.nombre} Apellido: {cocinero.apellido} Antiguedad: {cocinero.antiguedad} fechaDeNacimiento: {cocinero.fecha_de_nacimiento}"

    return HttpResponse(documento_texto)

def lavaplato(request):
    lavaplatos= LavaPlatos(nombre="Juan", apellido="Rossi", antiguedad="2020-3-11" , fechaDeNacimiento="1997-9-17" )
    lavaplatos.save()
    documento_texto = f">Lavaplatos: {lavaplatos.nombre} Apellido: {lavaplatos.apellido} Antiguedad: {lavaplatos.antiguedad} fechaDeNacimiento: {mozo.fecha_de_nacimiento}"

    return HttpResponse(documento_texto)

def inicio(request):
    return render(request,"App1/inicio.html")

def mozos (request):
    if request.method == 'POST':

        miFormulario = MozoFormulario(request.Post)

        print(miFormulario)
        
        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            mozo = Mozo (nombre=informacion['mozo'], apellido=informacion['apellido'],antiguedad=informacion['antiguedad'], fecha_de_nacimiento=informacion['fecha_de_nacimiento'])
            mozo.save()
            return render(request, "App1/?????") #a donde vuelve?
    else:
        miFormulario= MozoFormulario() #Formulario vacio
    return render(request,"App1/?????.html", {"miFormulario":miFormulario})

def Cocineros (request):
    if request.method == 'POST':

        miFormulario = CocineroFormulario(request.Post)

        print(miFormulario)
        
        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            cocinero = Cocinero (nombre=informacion['cocinero'], apellido=informacion['apellido'],antiguedad=informacion['antiguedad'], fecha_de_nacimiento=informacion['fecha_de_nacimiento'])
            cocinero.save()
            return render(request, "App1/?????") #a donde vuelve?
    else:
        miFormulario= CocineroFormulario() #Formulario vacio
    return render(request,"App1/?????.html", {"miFormulario":miFormulario})

def Lavaplatos (request):
    if request.method == 'POST':

        miFormulario = LavaplatosFormulario(request.Post)

        print(miFormulario)
        
        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            lavaplatos = LavaPlatos (nombre=informacion['cocinero'], apellido=informacion['apellido'],antiguedad=informacion['antiguedad'], fecha_de_nacimiento=informacion['fecha_de_nacimiento'])
            lavaplatos.save()
            return render(request, "App1/?????") #a donde vuelve?
    else:
        miFormulario= LavaplatosFormulario() #Formulario vacio
    return render(request,"App1/?????.html", {"miFormulario":miFormulario})

def buscar(request):
    if request.GET["apellido"]:

        apellido = request.GET['apellido']
        mozo = Mozo.objects.filter(apellido__icontains=apellido)

        return render (request, "App1/inicio.html",{"mozo":mozo, "apellido":apellido})
    else:

        respuesta = "No entraste datos"
        return HttpResponse(respuesta)






