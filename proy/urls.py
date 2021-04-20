from django.urls import path
from .views import (
    ProyListView, 
    ProyDetailView, 
    ProyCreateView, 
    ProyUpdateView,
    ProyDeleteView,


) 

urlpatterns = [
    path('opcion/<int:pk>/eliminar', ProyDeleteView.as_view(), name="eliminarJuego"),
    path('opcion/<int:pk>/editar', ProyUpdateView.as_view(), name="editarJuego"),
    path('opcion/NuevoJuego', ProyCreateView.as_view(), name="juegoNuevo"),
    path('opcion/<int:pk>/', ProyDetailView.as_view(), name='detalleJuego'),
    path('', ProyListView.as_view(), name='principal')

]