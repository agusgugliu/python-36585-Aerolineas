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
]