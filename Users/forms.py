from django.contrib.auth.forms import UserCreationForm
from Users.models import *
from django.contrib.auth.models import User

class EmpleadoForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super(EmpleadoForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].widget.attrs['placeholder'] = field

	def save(self, profile_callback=None):
		new_user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password1'])
		new_empleado=Persona(
			nombre=self.cleaned_data['nombre'],
			apellido=self.cleaned_data['apellido'],
			email=self.cleaned_data['email'],
			direccion=self.cleaned_data['direccion'],
			telefono=self.cleaned_data['telefono'],
			id_empleado=self.cleaned_data['id_empleado'],
			genero=self.cleaned_data['genero'],
			titulo_profesional=self.cleaned_data['titulo_profesional'],
			fecha_ingreso=self.cleaned_data['fecha_ingreso'],
			fecha_despido=self.cleaned_data['fecha_despido'],
			cargo=self.cleaned_data['cargo'],
			user=new_user
			)
		new_empleado.save()
		return new_user

	class Meta:
		model=Persona
		fields=('nombre','apellido','email','direccion','telefono','id_empleado','genero','titulo_profesional','fecha_ingreso','fecha_despido','cargo',
				'username','password1','password2',)

class ClienteForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super(ClienteForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].widget.attrs['placeholder'] = field
		self.fields.pop('username')
		self.fields.pop('password1')
		self.fields.pop('password2')

	def save(self, profile_callback=None):
		new_cliente=Persona(
			nombre=self.cleaned_data['nombre'],
			email=self.cleaned_data['email'],
			direccion=self.cleaned_data['direccion'],
			actividad_comercial=self.cleaned_data['actividad_comercial'],
			telefono=self.cleaned_data['telefono'],
			tipo_cliente=self.cleaned_data['tipo_cliente']
			)
		new_cliente.save()
		return new_cliente

	class Meta:
		model=Persona
		fields=('nombre','email','direccion','telefono','actividad_comercial','tipo_cliente',)
