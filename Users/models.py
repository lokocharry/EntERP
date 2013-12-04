# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from RecursosHumanos.models import Cargo

class Persona(models.Model):
	nombre=models.CharField(max_length=15)
	email=models.EmailField(max_length=75)
	direccion=models.CharField(max_length=15)
	telefono=models.CharField(max_length=15)

	#empleado
	GENERO=(
		('M', 'Masculino'),
		('F', 'Femenino'),
	)
	apellido=models.CharField(max_length=15, null=True, blank=True)
	id_empleado=models.IntegerField(null=True, blank=True, unique=True)
	genero=models.CharField(max_length=20, choices=GENERO, null=True, blank=True)
	titulo_profesional=models.CharField(max_length=20, null=True, blank=True)
	fecha_ingreso=models.DateField(null=True, blank=True)
	fecha_despido=models.DateField(null=True, blank=True)
	cargo=models.ForeignKey(Cargo, null=True, blank=True)
	user=models.OneToOneField(User, unique=True, null=True, blank=True)

	#cliente
	actividad_comercial=models.CharField(max_length=20, null=True, blank=True)
	TIPO_CLIENTE=(
		('P', 'Persona'),
		('E', 'Empresa'),
	)
	tipo_cliente=models.CharField(max_length=20, choices=TIPO_CLIENTE, null=True, blank=True)

	class Meta:
		permissions = (("can_view_about", "Can view acerca de"),)

	def __unicode__(self):
		if self.apellido is None:
			return self.nombre
		else:
			return '%s %s' % (self.nombre, self.apellido)
