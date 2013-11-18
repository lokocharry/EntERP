from django import forms
from Logistica.models import *
from Users.models import *
from django.contrib.admin import widgets
from Logistica.models import *

class HistorialTrabajoForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(HistorialTrabajoForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].widget.attrs['placeholder'] = field
		self.fields['empleado'].queryset = Persona.objects.exclude(tipo_cliente__isnull=False)
			
	class Meta:
		model=Historial_Trabajo

class PagosODescuentosForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(PagosODescuentosForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].widget.attrs['placeholder'] = field
		self.fields['empleado'].queryset = Persona.objects.exclude(tipo_cliente__isnull=False)

	class Meta:
		model=Pagos_O_Descuentos