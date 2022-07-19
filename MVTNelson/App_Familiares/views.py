from django.http import HttpResponse
from django.shortcuts import render
from App_Familiares.models import Familiar

# Create your views here.

def familiar(self, nombre, edad, fecha_nacimiento):

    familiar = Familiar(nombre=nombre, edad=edad, fecha_nacimiento=fecha_nacimiento)
    familiar.save()

    return HttpResponse(f"""
        <p>El familiar {familiar.nombre}, edad de {familiar.edad} años, fecha de nacimiento {familiar.fecha_nacimiento} fue agregado a la base de datos.</p>
    """)
    

def lista_familiares(self):

    lista = Familiar.objects.all()

    return render(self, "lista-familiares.html", {"lista_familiares": lista})