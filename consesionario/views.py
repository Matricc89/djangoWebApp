from django.shortcuts import render, redirect
from . models import *
from . forms import *
# Create your views here.

def home(req):
    return render(req,'consesionario/index.html')



def customers_view(request):
     
     if request.method == "GET":
        form = ClienteFormulario()
        return render(
             request,
             "consesionario/add_customer.html",
             context={"form": form}
         )
     else:
       
         formulario = ClienteFormulario(request.POST)
         if formulario.is_valid():
            informacion = formulario.cleaned_data

         modelo = Cliente(nombre=request.POST['nombre'],apellido=request.POST['apellido'],edad=request.POST['edad'])
         modelo.save()
        
     return redirect("consesionario:list")

def garages_view(request):
     
     if request.method == "GET":
        form = SucursalFormulario()
        return render(
             request,
             "consesionario/add_garage.html",
             context={"form": form}
         )
     else:
       
         formulario = SucursalFormulario(request.POST)
         if formulario.is_valid():
            informacion = formulario.cleaned_data

         modelo = Sucursal(nombre=request.POST['nombre'],direccion=request.POST['direccion'])
         modelo.save()
        
     return redirect("consesionario:list")

def cars_view(request):
     
     if request.method == "GET":
        form = AutoFormulario()
        return render(
             request,
             "consesionario/add_car.html",
             context={"form": form}
         )
     else:
       
         formulario = AutoFormulario(request.POST)
         if formulario.is_valid():
            informacion = formulario.cleaned_data

         modelo = Auto(marca=request.POST['marca'],modelo=request.POST['modelo'],color=request.POST['color'],precio=request.POST['precio'])
         modelo.save()
        
     return redirect("consesionario:list")



def list(req):


    cars = Auto.objects.all()
    customers = Cliente.objects.all()
    garages = Sucursal.objects.all()

    print(cars)
    

    return render(req,'consesionario/list.html',{"cars":cars,"customers":customers,"garages":garages})

def search_view(request):

    if request.method == "GET":
        form = BuscarFormulario()
        return render(
            request,
            "consesionario/search.html",
            context={"form": form}
        )
    else:
        formulario = BuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            autos_filtrados = []
            for auto in Auto.objects.filter(marca__iexact=informacion["marca"].upper()):
                autos_filtrados.append(auto)

            contexto = {"Autos": autos_filtrados}
            return render(request, "consesionario/autos_list.html", contexto)
        

def delete_car(request, id):
    try:
        car = Auto.objects.get(id=id)
        car.delete()
        return redirect("consesionario:list")
    except Auto.DoesNotExist:
        
        return redirect("consesionario:list")
    
def delete_garage(request, id):
    try:
        garage = Sucursal.objects.get(id=id)
        garage.delete()
        return redirect("consesionario:list")
    except Sucursal.DoesNotExist:
        
        return redirect("consesionario:list")    