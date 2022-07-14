from django.urls import path
from App1 import views


urlpatterns = [
    path('',views.inicio,name="Inicio"),#  Esta es la primer view
    path('mozos/',views.mozos,name="Mozos"),
    path('cocineros/',views.cocineros,name="Cocineros"),
    path('lavaplatos/',views.lavaplatos,name="Lavaplatos"),
    path('buscar/',views.buscar),
    path('busquedaMozos/',views.busquedaMozos,name='busquedaMozos'),
    path('buscarA/', views.buscarA,name='buscarA'),
]