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
    
    familia =[flia1,flia2,flia3]
    msg=[]
    
    for persona in familia:
        persona.save()
        cadena_Texto = f"Se agregó a {persona.nombre} {str(persona.apellido)} a la base de datos. <br>"
        msg.append(cadena_Texto)
    
    '''
    flia1.save() # ->  Guarda en base de datos
    #msgs = {'mensaje':msg}
    cadena_Texto1 = f" {flia1.nombre} {str(flia1.apellido)} ."
    flia2.save()
    cadena_Texto2 = f" {flia2.nombre} {str(flia2.apellido)} ."
    flia3.save()
    cadena_Texto3 = f" {flia3.nombre} {str(flia3.apellido)} ."
    #msg.append(cadena_Texto)
    
    msgs={"flia1":cadena_Texto1,"flia2":cadena_Texto2,"flia3":cadena_Texto3}
    
    plantilla = loader.get_template("template1.html")

    documento= plantilla.render(msgs)

    return HttpResponse(documento)

    '''

    return HttpResponse(msg)
    # Hay que mostrar los tres objetos que creo
       
    

