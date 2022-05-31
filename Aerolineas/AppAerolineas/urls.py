from django.urls import path
from AppAerolineas import views
#-------------------------------
urlpatterns = [
    path('', views.inicio, name="index"),
    path('aeropuertos/', views.aeropuertos_list, name='aeropuertos'),
    path('agregar_aeropuerto/', views.aeropuertos_add, name='agregar_aeropuerto'),
    path('borrar_aeropuerto/<identity>', views.aeropuertos_delete, name='borrar_aeropuerto'),
    path('buscar_aeropuerto_pais/', views.pais_aerop_search, name="pais_aerop_search"),
    path("buscar_aeropuerto_prov/", views.prov_aerop_search, name="prov_aerop_search"),
    path('aerolineas/', views.aerolineas_list, name = 'aerolineas'),
    path('agregar_aerolinea/', views.aerolineas_add, name='agregar_aerolinea'),
    path('borrar_aerolinea/<identity>', views.aerolineas_delete, name='borrar_aerolinea'),
    path('buscar_aerolinea_pais/', views.pais_aerolinea_search, name = 'pais_aerolinea_search'),
    path('buscar_alianza_aerolinea/', views.alianza_aerolinea_search, name = 'alianza_aerolinea_search'),
]