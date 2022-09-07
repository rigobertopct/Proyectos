from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView

from App.forms import ProyectoForm
from App.models import Proyecto
from App.forms import AnexoForm
from App.models import Anexo
from App.forms import ServicioForm
from App.models import Servicio





class HomeView(ListView):
    model = Proyecto
    template_name = 'index.html'

    def get_queryset(self):
        return Proyecto.objects.all()



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios'] = Servicio.objects.all()
        return context

class ProyectoCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'crear.html'


class AnexoCreateView(CreateView):
    model = Anexo
    form_class = AnexoForm
    template_name = 'crear.html'

class ServicioCreateView(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'crear.html'