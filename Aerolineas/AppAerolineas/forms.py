# IMPORTS
from django import forms
#-----------------------
#-----------------------
# AEROPUERTOS
class AeropuertosForm(forms.Form):
    nombre = forms.CharField(label="Nombre del Aeropuerto", max_length=100)
    siglas = forms.CharField(label="Siglas del Aeropuerto", max_length=5)
    pais = forms.CharField(label="País del Aeropuerto", max_length=50)
    estado = forms.CharField(label="Provincia del Aeropuerto", max_length=50)
    internacional = forms.CharField(label="¿Es internacional? [SI/NO]", max_length=5)
    año_inauguracion = forms.IntegerField(label="Año de Inauguración del Aeropuerto", widget=forms.NumberInput(attrs={'placeholder':1900}))

class BuscarPaisForm(forms.Form):
    pais_a_buscar = forms.CharField(label="Buscar Pais", max_length=50)

class BuscarProvinciaForm(forms.Form):
    provincia_a_buscar = forms.CharField(label="Buscar Provincia", max_length=50)

#-----------------------
# AEROLINEAS
class AerolineasForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la Aerolínea", max_length=50)
    siglas = forms.CharField(label="Siglas de la Aerolínea", max_length=10)
    sede = forms.CharField(label="País de la Aerolínea", max_length=50)
    alianza = forms.CharField(label="Alianza de la Aerolínea", max_length=50)
    año_fundacion = forms.IntegerField(label="Año de Fundación de la Aerolínea", widget=forms.NumberInput(attrs={'placeholder':1900}))

class BuscarAlianzaForm(forms.Form):
    alianza_a_buscar = forms.CharField(label="Buscar Alianza", max_length=50)

#-----------------------
# VUELOS
class VuelosForm(forms.Form):
    aerolinea_siglas = forms.CharField(label="Siglas de la Aerolínea", max_length=50)
    vuelo_numero = forms.CharField(label="Numero de Vuelo", max_length=10)
    fecha_vuelo = forms.DateField(label="Fecha del Vuelo", input_formats=["%d/%m/%Y"], widget=forms.TextInput(attrs={'placeholder':'25/09/2022'}))
    hora_vuelo = forms.IntegerField(label="Hora del Vuelo (HHMM)", widget=forms.NumberInput(attrs={'placeholder':1630}))
    aeropuerto_origen = forms.CharField(label="Aeropuerto de Origen", max_length=5)
    aeropuerto_destino = forms.CharField(label="Aeropuero de Destino", max_length=5)
    duracion_vuelo = forms.IntegerField(label="Duración del Vuelo (HHMM)", widget=forms.NumberInput(attrs={'placeholder':830}))

class BuscarVueloForm(forms.Form):
    vuelo_a_buscar = forms.CharField(label="Buscar Vuelo", max_length=10)

class BuscarOrigenForm(forms.Form):
    origen_a_buscar = forms.CharField(label="Buscar Origen", max_length=5)

class BuscarDestinoForm(forms.Form):
    destino_a_buscar = forms.CharField(label="Buscar Destino", max_length=5)