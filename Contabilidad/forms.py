from django import forms
from Contabilidad.models import *
from Users.models import *
from django.contrib.admin import widgets  

class ClienteForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ClienteForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].widget.attrs['placeholder'] = field
			
	class Meta:
		model=Persona

class ProductoForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ProductoForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].widget.attrs['placeholder'] = field

	class Meta:
		model=Producto

class FacturaForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(FacturaForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].widget.attrs['placeholder'] = field
		self.fields['empleado'].queryset = Persona.objects.exclude(tipo_cliente__isnull=False)
		self.fields['cliente'].queryset = Persona.objects.exclude(tipo_cliente__isnull=True)

	class Meta:
		model=Factura

class CuentaForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(CuentaForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].widget.attrs['placeholder'] = field

	class Meta:
		model=Cuenta

class SubCuentaForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(SubCuentaForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].widget.attrs['placeholder'] = field

	class Meta:
		model=SubCuenta

class LiquidacionForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(LiquidacionForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].widget.attrs['placeholder'] = field
		self.fields['empleado'].queryset = Persona.objects.exclude(tipo_cliente__isnull=False)

	class Meta:
		model=Liquidacion
		exclude = ['valor']