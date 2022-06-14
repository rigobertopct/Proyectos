from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView

from App.forms import ProyectoForm
from App.models import Proyecto


class ProyectoListView(ListView):
    model = Proyecto
    template_name = 'index.html'

    def get_queryset(self):
        return Proyecto.objects.all()
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return context

class ProyectoCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'crear.html'
