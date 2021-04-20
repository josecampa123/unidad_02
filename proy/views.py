from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Juegos, Organizadores, Tienda

class ProyListView(ListView):
    model = Juegos
    template_name = 'principal.html'
    context_object_name = 'doc'


class ProyDetailView(DetailView):
    model = Juegos
    template_name = "detalleJuego.html"
    context_object_name = 'doc'

class ProyCreateView(CreateView):
    model = Juegos
    template_name = "juegoNuevo.html"
    fields = '__all__'

class ProyUpdateView(UpdateView):
    model = Juegos
    template_name = 'editarJuego.html'
    fields = ['juego','descripcion']

class ProyDeleteView(DeleteView):
    model = Juegos
    template_name = 'eliminarJuego.html'
    context_object_name = 'doc'
    success_url = reverse_lazy('principal')

