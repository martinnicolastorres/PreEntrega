from django.shortcuts import render,  HttpResponse
from django.http.request import QueryDict
from AppCoder.models import *
from django.http import HttpResponse
from AppCoder.forms import EventoFormulario, PaginaFormulario
#from AppCoder.forms import

# Create your views here.
def seguidores(request):
    seguidores = Seguidores(nombre="Martins",apellido="Herrera", email="martinh123@gmail.com")
    seguidores.save()

    documentoDeTexto = f"--->seguidor: {seguidores.nombre} {seguidores.apellido}, email: {seguidores.email}"

    return HttpResponse(documentoDeTexto)


def inicio(request):

    return render(request, "AppCoder/Inicio.html")

def eventos(request):
    if request.method == 'POST':

            miFormulario = EventoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                informacion = miFormulario.cleaned_data

                eventos = Eventos (nombre=informacion['evento'], tema=informacion['tema'], integrantes=informacion['integrantes'],
                fechaini=informacion['fechaini'], fechafin=informacion['fechafin']) 

                eventos.save()

                return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

    else: 

            miFormulario= EventoFormulario() #Formulario vacio para construir el html

    return render(request, "AppCoder/Eventos.html", {"miFormulario":miFormulario})

# PAGINAS

def paginas(request):
    if request.method == 'POST':

            miFormulario = PaginaFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                informacion = miFormulario.cleaned_data

                paginas = Paginas (nombre=informacion['evento'], tema=informacion['tema'], integrantes=informacion['integrantes']) 

                paginas.save()

                return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

    else: 

            miFormulario= PaginaFormulario() #Formulario vacio para construir el html

    return render(request, "AppCoder/Paginas.html", {"miFormulario":miFormulario})

def buscar(request):

    if  request.GET["Paginas"]:

            nombre = request.GET['nombre'] 
            tema= tema.objects.filter(tema__icontains=nombre)

            return render(request, "AppCoder/inicio.html", {"paginas":Paginas, "tema":tema})

    else: 

	    respuesta = "No enviaste datos"
    
    return HttpResponse (respuesta)