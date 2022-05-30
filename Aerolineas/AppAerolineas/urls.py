from django.urls import path
from AppAerolineas import views
#-------------------------------
urlpatterns = [
    path('', views.inicio, name="index"),
]