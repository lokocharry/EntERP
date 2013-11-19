# -*- encoding: utf-8 -*-
from django.db import models
from RecursosHumanos.models import *
from Users.models import *

class Historial_Trabajo(models.Model):
	fecha_inicio=models.DateField()
	fecha_fin=models.DateField()
	empleado=models.ForeignKey(Persona)
	cargo=models.ForeignKey(Cargo)

	def __unicode__(self):
		return '%s %s %s - %s' % (self.empleado.nombre, self.empleado.apellido_empleado, self.fecha_inicio, self.fecha_fin)

class Pagos_O_Descuentos(models.Model):
	empleado=models.ForeignKey(Persona)
	descripcion=models.CharField(max_length=20)
	valor=models.IntegerField()
	fecha=models.DateField()

	def __unicode__(self):
		return '%s %s %s' % (self.empleado.nombre, self.empleado.apellido, self.valor)