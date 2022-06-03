# IMPORTS
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from AppAerolineas.models import Aeropuertos, Aerolineas, Vuelos
from AppAerolineas.forms import AeropuertosForm, BuscarPaisForm, BuscarProvinciaForm, AerolineasForm, BuscarPaisAerolineaForm, BuscarAlianzaForm, VuelosForm, BuscarVueloForm, BuscarOrigenForm, BuscarDestinoForm
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
        'aeropuertos':aeropuerto,
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
            Aeropuertos(nombre=nombre.title(), siglas=siglas.upper(), pais=pais.upper(), estado=estado.title(), internacional=internacional.upper(), año_inauguracion=año_inauguracion).save()
            return HttpResponseRedirect('/aeropuertos/')
    elif request.method == "GET":
        form = AeropuertosForm()
    else:
        return HttpResponseBadRequest('¡ERROR!\nNo conozco el método para este request.')
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
        return render(request, 'AppAerolineas/02_3_aeropuerto_search_pais.html', {'search_form':search_form})
    elif request.method == "POST":
        search_form = BuscarPaisForm(request.POST)
        if search_form.is_valid():
            pais_a_buscar = search_form.cleaned_data['pais_a_buscar']
            paises = Aeropuertos.objects.filter(pais__icontains=pais_a_buscar)
        return render(request, 'AppAerolineas/02_1_aeropuerto_list.html', {'aeropuertos':paises})

def prov_aerop_search(request):
    if request.method == "GET":
        prov_form = BuscarProvinciaForm()
        return render(request, 'AppAerolineas/02_4_aeropuerto_search_provincia.html', {'prov_form':prov_form})
    elif request.method == "POST":
        prov_form = BuscarProvinciaForm(request.POST)
        if prov_form.is_valid():
            provincia_a_buscar = prov_form.cleaned_data['provincia_a_buscar']
            provincias = Aeropuertos.objects.filter(estado__icontains=provincia_a_buscar)
        return render(request, 'AppAerolineas/02_1_aeropuerto_list.html', {'aeropuertos':provincias})

def aeropuerto_upd(request, identity):
    aeropuerto = Aeropuertos.objects.get(id=identity)
    if request.method == "POST":
        form = AeropuertosForm(request.POST)
        print(form)
        if form.is_valid():
            data = form.cleaned_data
            aeropuerto.nombre = data['nombre']
            aeropuerto.siglas = data['siglas']
            aeropuerto.pais = data['pais']
            aeropuerto.estado = data['estado']
            aeropuerto.internacional = data['internacional']
            aeropuerto.año_inauguracion = data['año_inauguracion']
            aeropuerto.save()
            return render(request, "AppAerolineas/00_index.html")
    else:
        form = AeropuertosForm(initial={'nombre':aeropuerto.nombre, 'siglas':aeropuerto.siglas, 'pais':aeropuerto.pais, 'estado':aeropuerto.estado, 'internacional':aeropuerto.internacional,'año_inauguracion':aeropuerto.año_inauguracion})
    return render(request, 'AppAerolineas/02_5_aeropuerto_update.html', {'form':form, 'identity':identity})

#-----------------------------
# AEROLINEAS
def aerolineas_list(request):
    aerolinea = Aerolineas.objects.all()
    template = loader.get_template('AppAerolineas/03_1_aerolinea_list.html')
    context = {
        'aerolineas':aerolinea,
    }
    return HttpResponse(template.render(context,request))

def aerolineas_add(request):
    if request.method == "POST":
        form = AerolineasForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            siglas = form.cleaned_data['siglas']
            sede = form.cleaned_data['sede']
            alianza = form.cleaned_data['alianza']
            año_fundacion = form.cleaned_data['año_fundacion']
            Aerolineas(nombre=nombre.upper(), siglas=siglas.upper(), sede=sede.upper(), alianza=alianza, año_fundacion=año_fundacion).save()
            return HttpResponseRedirect('/aerolineas/')
    elif request.method == "GET":
            form = AerolineasForm()
    else:
        return HttpResponseBadRequest('¡ERROR!\nNo conozco el método para este request.')
    return render(request, 'AppAerolineas/03_2_aerolinea_load.html', {'form':form})
   
def aerolineas_delete(request, identity):
    if request.method == "GET":
        aerolinea = Aerolineas.objects.filter(id=int(identity)).first()
        if aerolinea:
            aerolinea.delete()
        return HttpResponseRedirect('/aerolineas/')
    else:
        return HttpResponseBadRequest('¡ERROR!\nNo conozco el método para este request.')

def pais_aerolinea_search(request):
    if request.method == "GET":
        search_form = BuscarPaisAerolineaForm()
        return render(request, 'AppAerolineas/03_3_aerolinea_search_pais.html', {'search_form':search_form})
    elif request.method == "POST":
        search_form = BuscarPaisAerolineaForm(request.POST)
        if search_form.is_valid():
            pais_aerolinea_a_buscar = search_form.cleaned_data['pais_aerolinea_a_buscar']
            paises_aerolineas = Aerolineas.objects.filter(sede__icontains=pais_aerolinea_a_buscar)
        return render(request, 'AppAerolineas/03_1_aerolinea_list.html', {'aerolineas':paises_aerolineas})

def alianza_aerolinea_search(request):
    if request.method == "GET":
        search_form = BuscarAlianzaForm()
        return render(request, 'AppAerolineas/03_4_aerolinea_search_alianza.html', {'search_form':search_form})
    elif request.method == "POST":
        search_form = BuscarAlianzaForm(request.POST)
        if search_form.is_valid():
            alianza_a_buscar = search_form.cleaned_data['alianza_a_buscar']
            alianzas_aerolineas = Aerolineas.objects.filter(alianza__icontains=alianza_a_buscar)
        return render(request, 'AppAerolineas/03_1_aerolinea_list.html', {'aerolineas':alianzas_aerolineas})

#-----------------------------
# VUELOS
def vuelos_list(request):
    vuelo = Vuelos.objects.all()
    template = loader.get_template('AppAerolineas/04_1_vuelo_list.html')
    context = {
        'vuelos':vuelo,
    }
    return HttpResponse(template.render(context, request))

def vuelos_add(request):
    if request.method == "POST":
        form = VuelosForm(request.POST)
        if form.is_valid():
            aerolinea_siglas = form.cleaned_data['aerolinea_siglas']
            vuelo_numero = form.cleaned_data['vuelo_numero']
            fecha_vuelo = form.cleaned_data['fecha_vuelo']
            hora_vuelo = form.cleaned_data['hora_vuelo']
            aeropuerto_origen = form.cleaned_data['aeropuerto_origen']
            aeropuerto_destino = form.cleaned_data['aeropuerto_destino']
            duracion_vuelo = form.cleaned_data['duracion_vuelo']
            Vuelos(aerolinea_siglas=aerolinea_siglas.upper(), vuelo_numero=vuelo_numero, fecha_vuelo=fecha_vuelo, hora_vuelo=hora_vuelo, aeropuerto_origen=aeropuerto_origen.upper(), aeropuerto_destino=aeropuerto_destino.upper(), duracion_vuelo=duracion_vuelo).save()
            return HttpResponseRedirect('/vuelos/')
    elif request.method == "GET":
        form = VuelosForm()
    else:
        return HttpResponseBadRequest('¡ERROR!\nNo conozco el método para este request.')
    return render(request, 'AppAerolineas/04_2_vuelo_load.html', {'form':form})

def vuelos_delete(request, identity):
    if request.method == "GET":
        vuelo = Vuelos.objects.filter(id=int(identity)).first()
        if vuelo:
            vuelo.delete()
        return HttpResponseRedirect('/vuelos/')
    else:
        return HttpResponseBadRequest('¡ERROR!\nNo conozco el método para este request.')

def vuelo_search(request):
    if request.method == "GET":
        search_form = BuscarVueloForm()
        return render(request, 'AppAerolineas/04_3_vuelo_search_vuelo.html', {'search_form':search_form})
    elif request.method == "POST":
        search_form = BuscarVueloForm(request.POST)
        if search_form.is_valid():
            vuelo_a_buscar = search_form.cleaned_data['vuelo_a_buscar']
            vuelos = Vuelos.objects.filter(vuelo_numero__icontains=vuelo_a_buscar)
        return render(request, 'AppAerolineas/04_1_vuelo_list.html', {'vuelos':vuelos})

def vuelo_origen_search(request):
    if request.method == "GET":
        search_form = BuscarOrigenForm()
        return render(request, 'AppAerolineas/04_3_vuelo_search_origen.html', {'search_form':search_form})
    elif request.method == "POST":
        search_form = BuscarOrigenForm(request.POST)
        if search_form.is_valid():
            origen_a_buscar = search_form.cleaned_data['origen_a_buscar']
            origenes = Vuelos.objects.filter(aeropuerto_origen__icontains=origen_a_buscar)
        return render(request, 'AppAerolineas/04_1_vuelo_list.html', {'vuelos':origenes})

def vuelo_destino_search(request):
    if request.method == "GET":
        search_form = BuscarDestinoForm()
        return render(request, 'AppAerolineas/04_5_vuelo_search_destino.html', {'search_form':search_form})
    elif request.method == "POST":
        search_form = BuscarDestinoForm(request.POST)
        if search_form.is_valid():
            destino_a_buscar = search_form.cleaned_data['destino_a_buscar']
            destinos = Vuelos.objects.filter(aeropuerto_destino__icontains=destino_a_buscar)
        return render(request, 'AppAerolineas/04_1_vuelo_list.html', {'vuelos':destinos})