
from django import forms
from .models import SolicitudMantenimiento

class SolicitudMantenimientoForm(forms.ModelForm):
    class Meta:
        model = SolicitudMantenimiento
        fields = ['maquina', 'averia', 'descripcion']
