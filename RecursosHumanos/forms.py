from django import forms
from Users.models import *
from django.contrib.admin import widgets
from RecursosHumanos.models import *

class DepartamentoForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(DepartamentoForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].widget.attrs['placeholder'] = field
			
	class Meta:
		model=Departamento

class CargoForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(CargoForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].widget.attrs['placeholder'] = field

	class Meta:
		model=Cargo