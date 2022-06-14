from django.forms import ModelForm

from App.models import Proyecto


class ProyectoForm(ModelForm):
    class Meta:
        model=Proyecto
        fields='__all__'
