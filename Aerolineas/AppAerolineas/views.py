# IMPORTS
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from AppAerolineas.models import Aeropuertos, Aerolineas, Vuelos
from AppAerolineas.forms import AeropuertosForm, BuscarPaisForm, BuscarProvinciaForm, AerolineasForm, BuscarAlianzaForm, VuelosForm, BuscarVueloForm, BuscarOrigenForm, BuscarDestinoForm
#-----------------------------
#-----------------------------
# INICIO
def inicio(request):
    template = loader.get_template('AppAerolineas/01_landing_page.html')
    context = {}
    return HttpResponse(template.render(context,request))


#-----------------------------
# AEROPUERTOS
def aeropuertos_list(request):
    aeropuerto = Aeropuertos.objects.all()
    template = loader.get_template('AppAerolineas/02_1_aeropuerto_list.html')
    context = {
        'aeropuerto':aeropuerto
    }
    return HttpResponse(template.render(context,request))



def aeropuertos_add(request):
    if request.method == "POST":
        form = AeropuertosForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            siglas = form.cleaned_data['siglas']
            pais = form.cleaned_data['pais']
            estado = form.cleaned_data['estado']
            internacional = form.cleaned_data['internacional']
            año_inauguracion = form.cleaned_data['año_inauguracion']
            
            Aeropuertos(nombre=nombre, siglas=siglas, pais=pais, estado=estado, internacional=internacional, año_inauguracion=año_inauguracion).save()
            
            return HttpResponseRedirect('/aeropuertos/')
    
    elif request.method == "GET":
        form = AeropuertosForm()
    
    else:
        return HttpResponseBadRequest('¡ERROR! No conozco el método para este request.')
    
    return render(request, 'AppAerolineas/02_2_aeropuerto_load.html', {'form':form})



def aeropuertos_delete(request,identity):
    if request.method == "GET":
        aeropuerto = Aeropuertos.objects.filter(id=int(identity)).first()
        if aeropuerto:
            aeropuerto.delete()
        return HttpResponseRedirect('/aeropuertos/')
    else:
        return HttpResponseBadRequest('¡ERROR!\nNo conozco el método para este request.')



def pais_aerop_search(request):
    if request.method == "GET":
        search_form = BuscarPaisForm()
        return render(request, 'AppAerolineas/02_3_aeropuerto_search.html', {'search_form':search_form})
    elif request.method == "POST":
        search_form = BuscarPaisForm(request.POST)
        if search_form.is_valid():
            pais_a_buscar = search_form.cleaned_data['pais_a_buscar']
            paises = Aeropuertos.objects.filter(pais__icontains=pais_a_buscar)
        return render(request, 'AppAerolineas/02_1_aeropuerto_list.html', {'paises':paises})



def estado_aerop_search(request):
    if request.method == "GET":
        search_form = BuscarPaisForm()
        return render(request, 'AppAerolineas/02_3_aeropuerto_search.html', {'search_form':search_form})
    elif request.method == "POST":
        search_form = BuscarProvinciaForm(request.POST)
        if search_form.is_valid():
            provincia_a_buscar = search_form.cleaned_data['provincia_a_buscar']
            provincias = Aeropuertos.objects.filter(estado__icontains=provincia_a_buscar)
        return render(request, 'AppAerolineas/02_1_aeropuerto_list.html', {'provincias':provincias})