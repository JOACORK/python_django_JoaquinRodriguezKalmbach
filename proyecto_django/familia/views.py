from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Familia
from django.template import Template, Context

# Create your views here.
def familia(request):
    flia1= Familia(nombre="Carolina",apellido="Estrada",edad=63,fecha_nacimiento="1959-01-03")
    flia2= Familia(nombre="Matías",apellido="Olivetti",edad=58,fecha_nacimiento="1964-04-10")
    flia3= Familia(nombre="Feli",apellido="Estrada Olivetti",edad=23,fecha_nacimiento="1999-07-25")

    flia1.save() 
    flia2.save()
    flia3.save()

    
    familia={"flia1":flia1,"flia2":flia2,"flia3":flia3}
    
    plantilla = loader.get_template("template1.html")

    documento= plantilla.render(familia)

    return HttpResponse(documento)


       
    

