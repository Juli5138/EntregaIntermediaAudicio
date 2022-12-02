from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Autor
from django.core import serializers
from AppCoder.forms import AutorFormulario

# Create your views here.
def inicio(request):
    return render(request,'AppCoder/inicio.html')

def autor(request):
    if request.method == "POST":
            miFormulario = AutorFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  #informacion = {"curso":"12313", "camada":1223,"numero_dia":1}
                  autor = Autor(autor=informacion["autor"], info=informacion["info"], orden=informacion["orden"])
                  autor.save()
                  return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = AutorFormulario()
 
    return render(request, "AppCoder/autores.html", {"miFormulario": miFormulario})


def profesores(request):
    return HttpResponse('Vista de profesores')

def autoresapi(request):
    autores_todos = Autor.objects.all()
    return HttpResponse(serializers.serialize('json', autores_todos))
